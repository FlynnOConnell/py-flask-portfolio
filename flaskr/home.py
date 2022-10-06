from flask import (
    Blueprint, flash, redirect, render_template,
    request, url_for, current_app, make_response)
from .cloud import get_bucket_images

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET', 'POST'])
def get_img():
    urls = [x for x in get_bucket_images()]
    return render_template('home/index.html', url=urls)