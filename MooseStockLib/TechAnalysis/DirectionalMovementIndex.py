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
        
        excel_writer = pd.ExcelWriter(filePath)
        df_DMI = pd.read_excel(filePath)
        #df_DMI = df_DMI.dropna()
        
        print(df_company)
        self.logger.info('[^] create DMI')