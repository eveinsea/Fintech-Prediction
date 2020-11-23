# -*- coding: utf-8 -*-
# here you will register all blueprint apps
#from .home import home
from .fintech import fintech_caller



def register_blueprint(app):
    app.register_blueprint(fintech_caller, url_prefix='')
