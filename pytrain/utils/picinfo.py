# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/21 9:06 AM
@Author  : dengwei
@File    : picinfo.py
'''
import os

import exifread
import re
import time


class PicInfoUtil:

    @classmethod
    def latitude_and_longitude_convert_to_decimal_system(cls, *arg):
        """
        经纬度转为小数, 作者尝试适用于iphone6、ipad2以上的拍照的照片，
        :param arg:
        :return: 十进制小数
        """
        return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)

    @classmethod
    def find_GPS_image(cls, pic_path):
        GPS = {}
        date = ''
        with open(pic_path, 'rb') as f:
            tags = exifread.process_file(f)
            for tag, value in tags.items():
                if re.match('GPS GPSLatitudeRef', tag):
                    GPS['GPSLatitudeRef'] = str(value)
                elif re.match('GPS GPSLongitudeRef', tag):
                    GPS['GPSLongitudeRef'] = str(value)
                elif re.match('GPS GPSAltitudeRef', tag):
                    GPS['GPSAltitudeRef'] = str(value)
                elif re.match('GPS GPSLatitude', tag):
                    try:
                        match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                        GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                    except:
                        deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                        GPS['GPSLatitude'] = cls.latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
                elif re.match('GPS GPSLongitude', tag):
                    try:
                        match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                        GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                    except:
                        deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                        GPS['GPSLongitude'] = cls.latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
                elif re.match('GPS GPSAltitude', tag):
                    GPS['GPSAltitude'] = str(value)
                elif re.match('.*Date.*', tag):
                    date = str(value)
        return {'GPS_information': GPS, 'date_information': date}

    @classmethod
    def get_file_create_time(cls, file_path):
        return time.localtime(os.stat(file_path).st_birthtime)

    @classmethod
    def get_file_modify_time(cls, file_path):
        return time.localtime(os.stat(file_path).st_mtime)


if __name__ == "__main__":
    print(PicInfoUtil.find_GPS_image("/Volumes/ntfs_dw/Photos1/2018/01/IMG_0090.HEIC"))