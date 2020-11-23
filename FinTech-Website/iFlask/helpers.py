# -*- coding: utf-8 -*-
"""
     Helpers
"""
from __future__ import with_statement
import unicodedata
import re
import os

from functools import wraps
from flask import session, url_for, redirect, request, flash
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

def static(filename):
    """Adds content versioning to static files by appending a last modification
    timestamp to the url"""
    filepath = os.path.join(os.path.dirname(__file__), 'static', filename)
    last_modification = '%d' % os.path.getmtime(filepath)
    return url_for('.static', filename=filename) + '?' + last_modification


def login_required(f):
    """Redirect to login page if user not logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Login required', 'error')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def normalize(string):
    """Unify string"""
    string = unicodedata.normalize("NFKD", unicode(string)).encode(
        "ascii", "ignore")
    string = re.sub(r"[^\w]+", " ", string)
    string = "-".join(string.lower().strip().split())
    return string


def normalize_tags(string):
    """Return a list of normalized tags from a string with comma separated
    tags"""
    tags = string.split(',')
    result = []
    for tag in tags:
        normalized = normalize(tag)
        if normalized and not normalized in result: 
            result.append(normalized)
    return result

def setJinJa2_template_path(loader,template_folder=None):
    if not template_folder:
        return
    import jinja2

    cwd = os.getcwd()
    template_path = os.path.join(cwd, 'iFlask', template_folder)
    my_loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(template_path),
        loader,
    ])

    return my_loader