# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:05:17 2018
"""
#@author: ME389019
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import os
import time
import smtplib


#import string
#duration = 'hours ago'
#from brorefresh import driver

driver = webdriver.Chrome(executable_path="C:\Python27\Oracle\chromedriver.exe")

driver.maximize_window()
#driver.get("https://10.12.253.72/cuadmin/home.do")
driver.get("https://google.com")

time.sleep(5) 
"""

#need to install drivers
import webbrowser as wb,sys
print sys.argv
wb.open('https://www.youtube.com')
address="khanna"
if len(sys.argv)>1:
        address=' '.join(sys.argv[1:])
wb.open('https://www.google.com/maps/search/'+address)