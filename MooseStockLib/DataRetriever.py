# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:47:22 2018

@author: Mussina
"""

import twstock
import logging

#import pandas as pd
#logging.config.fileConfig('./config/logconfig.ini')

class HisDataRetriever(object):
    #logging.config.fileConfig('.././config/logconfig.ini')
    
    def __init__(self, sid, logger=None):
        self.logger = logger or logging.getLogger("root")
        self.sid = sid
        self.stock = twstock.Stock(self.sid)
    
    def fetchLast31(self):
        self.logger.info('[v] fetch last 31 days data.')
        print("fetchLast31")
        #stock = twstock.Stock(sid)
        self.logger.info('[^] fetch last 31 days data.')
    
    def fetchSinceDate(self, year, month):
        result = self.stock.fetch_from(year, month)
        return result
    
    def getMoving_Avg(self, prices, day):
        return self.stock.moving_average(prices, day)
    