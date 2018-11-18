# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:52:52 2018

@author: Mussina
"""
import logging

class StockDataInitializer():
    def __init__(self,logger=None):
        self.data = []
        self.logger = logger or logging.getLogger("root")
    
    """
    iniial all companys data in CompanyData folder
    """
    def iniCompanyData(self, companys):
        self.logger.info('[v] initial company data.')
        print(companys)
        self.logger.info('[^] initial company data.')