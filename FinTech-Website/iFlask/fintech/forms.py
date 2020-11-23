# coding: utf-8

"""
    forms.py
    ~~~~~~~~
"""
# from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import IntegerField, FloatField, StringField, SubmitField, PasswordField, BooleanField
#from wtforms.validators import Required, EqualTo

class FeatureForm(FlaskForm):
    """ Feature Form"""
    term = IntegerField('Term 36 or 60')
    loan_amnt = IntegerField('Loan Amount')
    int_rate = FloatField('Rate')
    fund_rate = IntegerField('Alrady Funded')

    bc_open_to_buy = IntegerField('Revolving Credit Limit')
    total_il_high_credit_limit = IntegerField('otal Installment Limit')
    dti = IntegerField('Debt-to-Income Ratio')
    bc_util = IntegerField('Portion of Balances')
    annual_inc = IntegerField('Annual Income')

    go = SubmitField('Submit')


class UploadForm(FlaskForm):
    DataFile = FileField('Your data file', validators=[
        FileRequired(),
        FileAllowed(['csv', 'txt'], 'plain text file only!')
    ])
