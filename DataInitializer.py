# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:52:52 2018

@author: Mussina
"""
import logging
import pandas as pd
from pathlib import Path

""" self lib """
from MooseStockLib.DataRetriever import HisDataRetriever


class StockDataInitializer():
    def __init__(self,logger=None):
        self.data = []
        self.logger = logger or logging.getLogger("root")
    
    """
    iniial all companys data in CompanyData folder
    """
    def iniCompanyData(self, companys):
        self.logger.info('[v] initial company data.')
        
        # loop all company's sid
        for sid in companys:
            self.logger.info('process...[%s]',sid)
            filePath = "./CompanyData/" + sid + ".xlsx"
            sid_file = Path(filePath)
            if not sid_file.is_file():
                self.logger.info("file not exist...please create .xlsx file first.")
                continue
            
            #start process 
            sid_df = pd.read_excel(filePath)
            dataRetrv = HisDataRetriever(sid)
            if sid_df.empty:
                self.logger.info('empty excel, download all data')
                hisData = dataRetrv.fetchSinceDate(2018, 11)
                print(hisData)
            else:
                self._findLatestDay(sid_df)
            #self._findLatestDay(sid_df)
                           
        self.logger.info('[^] initial company data.')
        
        
    def _findLatestDay(self, sid_df):
        print(sid_df)
        
        