# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:47:22 2018

@author: Mussina
"""

import twstock
import logging
import logging.config
#import pandas as pd

class HisDataRetriever():
    def __init__(self):
        logging.config.fileConfig('././config/logconfig.ini')
        self.logger = logging.getLogger('root')
    
    def fetchLast31(self, sid):
        self.logger.info('[v] fetch last 31 days data.')
        print("123")
        stock = twstock.Stock(sid)
        self.logger.info('[^] fetch last 31 days data.')
        return stock