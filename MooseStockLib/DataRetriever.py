# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:47:22 2018

@author: Mussina
"""

import twstock
#import pandas as pd

class HisDataRetriever():
    def __init__(self, logger):
        self.logger = logger
    
    def fetchLast31(self, sid):
        return twstock.Stock(sid)