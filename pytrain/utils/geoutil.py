# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/21 9:10 AM
@Author  : dengwei
@File    : geoutil.py
'''

import requests
import json


class GeoUtil:

    @staticmethod
    def find_address_from_GPS(self, latitude, longitude):
        """
        使用Geocoding API把经纬度坐标转换为结构化地址。
        :param GPS:
        :return:
        """
        secret_key = '273ea561fc6cf2fc908c2936a58cb4f2'             # 高德地图创应用的秘钥
        amap_api = "https://restapi.amap.com/v3/geocode/regeo?key={0}&location={1},{2}&output=JSON&radius=1000&extensions=all".format(
            secret_key, lng, lat)
        # print(amap_api)
        response = requests.get(amap_api)
        content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
        # print(content)
        baidu_map_address = json.loads(content)
        formatted_address = "{0}-{1}-{2}".format(
            baidu_map_address["regeocode"]["addressComponent"]["province"], baidu_map_address["regeocode"]["addressComponent"]["city"], baidu_map_address["regeocode"]["addressComponent"]["district"])
        return formatted_address