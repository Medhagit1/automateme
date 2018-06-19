# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:09:00 2018

@author: ME389019
"""

import requests as rq
res=rq.get('http://automatetheboringstuff.com/files/rj.txt')
len(res.text)
print(res.text[:300])  # downloads the contents of the website-- requests


#requests model useful when we have
""" 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import time
import smtplib"""

import time
from selenium import webdriver as wd
browser=wd.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')
browser.maximize_window()
browser.get("https://www.youtube.com/watch?v=6yPdo6iTTC4")
time.sleep(5) 

browser.minimize_window()

elem=browser.find_element_by_css_selector('p')
print(len(elem))
browser.close()