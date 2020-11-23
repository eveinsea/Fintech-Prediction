#-*- coding: utf-8 -*-
import os
from flask import Flask, request, abort
import logging
from logging.handlers import RotatingFileHandler

from .helpers import RegexConverter, setJinJa2_template_path
from .register_blueprint import register_blueprint

app = Flask(__name__,
        template_folder='templates',
        static_folder='static')

app.url_map.converters['regex'] = RegexConverter

# load config by py file
app.config.from_pyfile('config.py')

# load logger
if not os.path.exists('log'):
    os.mkdir('log')
handler = RotatingFileHandler('log/iflasker.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

register_blueprint(app)


