# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:28:21 2019

@author: Mussina
"""
import logging
import pandas as pd
from pathlib import Path

class DMI():
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger("root")
        
    def create_DMI_Index(self, df_company, company):
        self.logger.info('[v] create DMI')
        
        # --- read and pre-process --- #
        self.logger.info('DMI process...[%s]',company)
        filePath = "../../CompanyData/" + company + "_DMI.xlsx"
        sid_file = Path(filePath)
        if not sid_file.is_file():
            self.logger.info("file not exist...please create [%s] file first.",filePath)
            return
        
        #excel_writer = pd.ExcelWriter(filePath)
        df_DMI = pd.read_excel(filePath)
        
        #df_DMI = df_DMI.dropna()
        
        self._createDMI(df_company, df_DMI)
        
        #excel_writer.close()
        self.logger.info('[^] create DMI')
        
    def _createDMI(self, df_company, df_DMI):
        if df_DMI.last_valid_index() == None:
            dmi_idx = 0
        else:
            dmi_idx = df_DMI.last_valid_index() + 1
        
        row_num = len(df_company.index)
        for i in range(row_num):
            if i == 0:
                DM_plus = 0
            else:
                DM_plus = self._cal_DM_Plus(df_company.iloc[i]['最高價'], df_company.iloc[i-1]['最高價'])
            
            
                
            df_DMI.loc[dmi_idx] = [df_company.iloc[i]['日期'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最低價'],
                                   df_company.iloc[i]['收盤價'],
                                   DM_plus,
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價'],
                                   df_company.iloc[i]['最高價']                                
                                  ]
            #df_DMI.iloc[dmi_idx]['最低價'] = df_company.iloc[i]['最低價']
            dmi_idx += 1         
            # --- get start index --- #
            
        print(df_DMI)
        #--- set data to dataframe ---#
            #df_company['最高價']
    def _cal_DM_Plus(Highest_price, pre_Highest_price):
        DM_plus = Highest_price - pre_Highest_price
        if DM_plus < 0:
            DM_plus = 0
        return DM_plus
    
    
    
    
    
    
    