#-*- coding: utf-8 -*-
from flask import Blueprint


fintech_caller = Blueprint('fintech', __name__, template_folder='templates')

from . import views

