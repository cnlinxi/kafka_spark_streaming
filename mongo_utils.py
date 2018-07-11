# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 17:49
# @Author  : MengnanChen
# @FileName: mongo_utils.py
# @Software: PyCharm Community Edition

'''
tools of mongodb
'''

import pymongo
from pymongo import MongoClient

class mongo_utils():
    @staticmethod
    def insert_data(data_dict:dict):
        conn = MongoClient('localhost', 27017)
        db = conn.mydb
        db.myset.insert(data_dict)
        conn.close()

    @staticmethod
    def query_last_row(uid:str)->dict:
        conn = MongoClient('localhost', 27017)
        db=conn.mydb
        cur=db.myset.find({'uid':uid}).sort('timestamp',pymongo.DESCENDING).limit(1)
        conn.close()
        # e.g.: {'_id': ObjectId('5b45c25f8650f8e6e4b74245'), 'uid': 'test', 'timestamp': '2018-07-11 16:39:59',
        # 'steps': '103','heart_rate':50}
        return cur[0]