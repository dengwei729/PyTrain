# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/21 9:07 AM
@Author  : dengwei
@File    : md5.py
'''


import hashlib

def getmd5(file):
    m = hashlib.md5()
    with open(file,'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code