# coding: utf-8

#import os
#import pickle
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class Base(object):
    __abstract__ = True

    def __init__(self):
        self.df = None
        self.trainedModel = ''
        # the model must be a object and it contain a named predict method
        self.model = None

    def load(self, path):
        #return pickle.load(open(path, 'r'))
        return pd.read_pickle(path)

    def loadDvalidFromDict(self, data):
        """exactly, need a method convet data to df object"""
        # return feature
        pass

    def loadDvalidFromFile(self, file, skiprows = 1):
        """load feature data from file"""
        # return dvalid
        pass

    def run(self, data):
        # load model from persistence file
        self.model = self.load(self.trainedModel)

        # prepare feature data
        if isinstance(data,dict):
            features = self.loadDvalidFromDict(data)

            result = self.predict(features)

            return result
        else:
            logger.error('Data must be a dict type')
            return None

    def predict(self, features):
        """
        Predict data
        Args:
            param: dvalid, data form
        """
        return self.model.predict(features)

    
