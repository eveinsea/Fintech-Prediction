# -*- coding: utf-8 -*-
import os
import datetime

DEBUG = True
TESTING = False

SECRET_KEY = 'you-will-never-guess'
CSRF_ENABLED = True

# site
SITE_TIME = datetime.datetime.today()

#: session
SESSION_COOKIE_NAME = '_s'
# SESSION_COOKIE_SECURE = True
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

DATABASE_URI = 'sqlite://:memory:'

