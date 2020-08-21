# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/21 9:07 AM
@Author  : dengwei
@File    : md5.py
'''


import hashlib


class Md5Util:
    @staticmethod
    def get_file_md5(file):
        m = hashlib.md5()
        with open(file,'rb') as f:
            for line in f:
                m.update(line)
        md5code = m.hexdigest()
        return md5code

    @staticmethod
    def get_str_md5(string):
        m = hashlib.md5()
        m.update(string.encode("utf-8"))
        md5code = m.hexdigest()
        return md5code

if __name__ == "__main__":
    print(Md5Util.get_str_md5("test"))