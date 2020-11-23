# -*- coding: utf-8 -*-
import os
import logging
from flask import (
    jsonify,
    render_template, 
    request)

from .forms import UploadForm, FeatureForm
#from werkzeug.utils import secure_filename

from . import fintech_caller
from .model import Fintech

logger = logging.getLogger(__name__)


# handler for form
@fintech_caller.route('/', methods=('GET', 'POST'))
def form():
    form = FeatureForm()
    Datas = {}

    if form.is_submitted():

        Datas['int_rate'] = form.int_rate.data
        Datas['loan_amnt'] = form.loan_amnt.data
        Datas['term'] = 36 if form.term.data == None else 60
        Datas['fund_rate'] = form.fund_rate.data
        Datas['bc_open_to_buy'] = form.bc_open_to_buy.data
        Datas['total_il_high_credit_limit'] = form.total_il_high_credit_limit.data
        Datas['dti'] = form.dti.data
        Datas['annual_inc'] = form.annual_inc.data
        Datas['bc_util'] = form.bc_util.data

        fin = Fintech()
        res = fin.run(Datas)
        if res:
            result = {'status': 'success', 'data': format(res[0], '.3f')}   #float(round(res[0], 3))
        else:
            result = {'status': 'failed', 'data':''}

        return jsonify(result)
    return render_template('result.html', form=form)

# endpoint page
@fintech_caller.route('/')
def submit():
    return render_template('result.html')

