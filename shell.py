#!/usr/bin/env python
import os
import readline
from pprint import pprint
from app import *

app = application.create_app('settings')
os.environ['PYTHONINSPECT'] = 'True'
