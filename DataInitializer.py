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
            
            ### start process ###
            # --- read and pre-process --- #
            excel_writer = pd.ExcelWriter(filePath)
            sid_df = pd.read_excel(filePath)
            sid_df = sid_df.dropna()
            sid_df = sid_df.astype("float32", copy=False)
            
            # --- create data retrever
            dataRetrv = HisDataRetriever(sid)
            
            
            if sid_df.empty:
                self.logger.info('empty excel, download all data')
                
                hisData = dataRetrv.fetchSinceDate(2018, 11)
                
                # --- get price as list --- #
                prices = self._getClosePriceList(hisData)
                
                # --- get moving average --- #
                MA5 = dataRetrv.getMoving_Avg(prices, 5)
                MA10 = dataRetrv.getMoving_Avg(prices, 10)
                MA5 = self._reallocMA(MA5, len(hisData))
                MA10 = self._reallocMA(MA10, len(hisData))

                self._setFetchedData(sid_df,MA5,MA10, hisData)
                sid_df.to_excel(excel_writer, index=False)
                excel_writer.save()
                print(sid_df)
            else:
                self._findLatestDay(sid_df)
            #self._findLatestDay(sid_df)
                           
        self.logger.info('[^] initial company data.')
        
    def _setFetchedData(self, sid_df,MA5, MA10, hisData=None):
        # --- get start index --- #
        if sid_df.last_valid_index() == None:
            sIdx = 0
        else:
            sIdx = sid_df.last_valid_index() + 1
        print("sIdx:")
        print(sIdx)
        
        maIdx = 0
        for data in hisData:
            sid_df.loc[sIdx] = [data.date.strftime('%Y-%m-%d'),
                                data.close,
                                data.high,
                                data.low,
                                data.capacity / 1000,
                                MA5[maIdx],
                                MA10[maIdx]]
            sIdx = sIdx + 1
            maIdx = maIdx + 1
    
    ### re-allocate MA lenth
    def _reallocMA(self, MA, hisDataLength):
        diff_MA = hisDataLength - len(MA)  
        addiMA = []
        i = 0
        
        for i in range(diff_MA):
            if i < len(MA):
                addiMA.append(MA[i])
            else:
                addiMA.append(MA[-1])
                
        return addiMA + MA
                
    def _findLatestDay(self, sid_df):      
        print(sid_df)
    
    def _getClosePriceList(self, hisData):
        list = []
        for data in hisData:
            list.append(data.close)
            
        return list