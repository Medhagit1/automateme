# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 14:28:48 2018

@author: ME389019
"""

from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

items =[]

class Item(Resource):  # student class has copy of resouce class
    def get(self,name):
        for item in items:
            if item['name']==name:
                return item
        return {'item':'no such items'},404  # status code
    def post(self,name):
        item={'name':name,'price':12.00}
        items.append(item)
        return item,201   # I have returned what u wanted 
    
    #202 accepted the request sys will work on it.

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')
app.run(port=3000,debug =True)