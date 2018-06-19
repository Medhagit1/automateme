# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 14:57:55 2018

@author: ME389019
"""

import shelve
shelfFile =shelve.open('mydata2.txt')

shelfFile['cats']=['A','B','C','D']
shelfFile.close()


shelfFile =shelve.open('mydata2.txt')
shelfFile['cats']

import os
os.path.abspath('mydata2.txt')


list(shelfFile.keys())


x=os.walk('E:\EA\studies')
for i,j,k in x:
    print "folder name is"+i
    print "subfolder "+str(j)
    print "files"+str(k)
    
    
    
import requests as rq
res=rq.get('http://google.com')
len(res.text)
print res.text[:100]

import bs4
import requests

res=requests.get('https://www.amazon.in/gp/product/B075P6STZV/ref=ox_sc_act_title_1?smid=AZ0B7IP8OS3JT&psc=1',)
res.raise_for_status
soup=bs4.BeautifulSoup(res.text,'html.parser')
soup.select('#priceblock_saleprice')