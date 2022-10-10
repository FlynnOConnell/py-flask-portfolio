from __future__ import annotations
from typing import Generator, ClassVar
import os

from google.cloud import exceptions
from google.cloud import storage
from pathlib import Path

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\flynn\repos\web_dataviewer\JSON_credentials.json"

# client can be global?
client = storage.Client()


def check_bucket_exists(bucket) -> bool:
    """
    :param bucket: name of GCS bucket
    :type bucket:str
    :return: If bucket exists
    :rtype: Bool
    """
    try:
        client.get_bucket(bucket)
        return True
    except exceptions.NotFound:
        return False


def upload_to_bucket(filepath: str | Path, bucket: str = 'graphs-1551') -> None:
    """
    :param filepath: "local/path/to/file"
    :type filepath: str
    :param bucket: name of GCS bucket
    :type bucket:str
    :return: None
    :rtype: None
    """
    if not hasattr(filepath, 'stem'):
        filepath = Path(filepath)
    if not filepath.is_file():
        raise AttributeError('Given path is not a file.')
    # TODO: play around with adding different buckets
    bucket = client.get_bucket(bucket)
    blobs = list(client.list_blobs(bucket))
    # delete blobs previously in this bucket
    if blobs:
        bucket.delete_blobs(blobs)
    blob = bucket.blob(filepath.name)
    # we want only the ext, not the .ext for the content type
    blob.upload_from_filename(filepath, content_type=f'img/{filepath.suffix[1:]}')


def get_bucket_images(bucket: str = 'graphs-1551') -> Generator[str, None, None]:
    """
    :param bucket: name of GCS bucket
    :type bucket: str
    :return: list of images
    :rtype: list
    """
    blobs = []
    bucket = client.get_bucket(bucket)
    for blob in list(client.list_blobs(bucket)):
        yield blob.public_url


def get_bucket_captions(bucket: str = 'captions-1551') -> Generator[str, None, None]:
    """
    :param bucket: name of GCS bucket
    :type bucket: str
    :return: list of images
    :rtype: list
    """
    blobs = []
    bucket = client.get_bucket(bucket)
    for blob in list(client.list_blobs(bucket)):
        yield blob.public_url


exist = check_bucket_exists('graphs-1551')
