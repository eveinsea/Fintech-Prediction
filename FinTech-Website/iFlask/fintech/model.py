# coding: utf-8
from __future__ import division
import os
#import sys
import xgboost as xgb
import numpy as np

from .container.base import Base
# from fintech import app
# add a comment for test git


class Fintech(Base):
    def __init__(self):
        super(Fintech, self).__init__()
        # here, can overwrite trained modelFile if you wanna change modle
        self.trainedModel = os.path.join(os.getcwd(),'iFlask/fintech','model/model.pkl')

    def loadDvalidFromDict(self, data):
        """exactly, need a method convet data to df object"""
        # it will raise ValueError: If using all scalar values, you must must pass an index
        # reference: http://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe
        fPath = os.path.join(os.getcwd(),'iFlask/fintech','model/feature.pkl')

        feature = self.load(fPath)

        # fix feature
        feature['bc_open_to_buy'] = data['bc_open_to_buy']
        feature['total_il_high_credit_limit'] = data['total_il_high_credit_limit']
        feature['dti'] = data['dti']
        feature['annual_inc'] = data['annual_inc']
        feature['bc_util'] = data['bc_util']

        feature['int_rate'] = data['int_rate']/100
        # high wie
        if data['term'] == 36:
            feature['term_ 36 months'] = 1
            feature['term_ 60 months'] = 0
        else:
            feature['term_ 36 months'] = 0
            feature['term_ 60 months'] = 1

        feature['loan_amnt'] = data['loan_amnt']
        
        loan_rate = data['fund_rate']/100
        feature['funded_amnt'] = loan_rate * feature['loan_amnt']

        dtrain = xgb.DMatrix(feature, missing=np.NAN)

        return dtrain

