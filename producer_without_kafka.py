# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 17:10
# @Author  : MengnanChen
# @FileName: mongo_run.py
# @Software: PyCharm Community Edition

'''
simulator of producing data without kafka for debug
'''

from mongo_utils import mongo_utils
import time
import threading
import random

def produce_data():
    num_user = 2
    users = ['t1', 't2']

    def work(user_number):
        while True:
            data_dict = {
                'timestamp': str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                'uid': users[user_number],
                'heart_rate': random.randint(50, 70),
                'steps': random.randint(100, 1000)
            }
            mongo_utils.insert_data(data_dict)
            # print(data_dict)
            time.sleep(3)

    thread_list = [threading.Thread(target=work, args=(i,)) for i in range(num_user)]
    for thread in thread_list:
        thread.setDaemon(True)
        thread.start()
    time.sleep(60) # total running time

if __name__ == '__main__':
    produce_data()