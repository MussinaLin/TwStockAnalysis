# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:03:29 2018

@author: Mussina
"""
import configparser
import logging
import logging.config
import twstock

#self made module
from MooseStockLib import CompanyRevenue
# logger setting
logging.config.fileConfig("./config/logconfig.ini")
logger = logging.getLogger("root")

logging.info("===== System Start =====")

# config setting
logging.info("[v] read config")
config = configparser.ConfigParser()
config.read('./config/config.ini')
logging.info("[^] read config")

temp = config.get('Stock', 'ToBeAnalysisStock')
ToBeAnalysisStock = temp.split(",")
logging.info("ToBeAnalysisStock:%s",ToBeAnalysisStock)


#monthRevenue = CompanyRevenue.monthly_report(2018,10)
#print(monthRevenue)



logging.info("===== System End =====")