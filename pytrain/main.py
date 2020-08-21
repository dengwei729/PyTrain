# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/21 9:08 AM
@Author  : dengwei
@File    : main.py
'''

import os
import shutil
import time
import traceback
from pytrain.utils.picinfo import PicInfoUtil
from pytrain.utils.geoutil import GeoUtil
from pytrain.utils.md5 import Md5Util

if __name__ == "__main__":

    md5_dict_t = {}
    photo_path = "/Volumes/ntfs_dw/Photos"
    for root, dirs, files in os.walk("/Volumes/ntfs_dw/Photos/2019/12-未知位置"):
        for item in files:
            file_path = os.path.join(root, item)
            if not os.path.isfile(file_path):
                continue

            # 创建时间
            c_time = PicInfoUtil.get_file_create_time(file_path=file_path)
            c_time_y = time.strftime('%Y', c_time)
            # 修改时间
            m_time = PicInfoUtil.get_file_modify_time(file_path=file_path)
            m_time_y = time.strftime('%Y', m_time)
            # 当前时间
            currnet = time.localtime()
            currnet_y = time.strftime('%Y', currnet)

            if int(currnet_y) - int(c_time_y) > 0:
                create_time = c_time
            else:
                create_time = m_time
            y = time.strftime('%Y', create_time)
            m = time.strftime('%m', create_time)

            try:
                GPS_info = PicInfoUtil.find_GPS_image(pic_path=file_path)  # 照片
                if not GPS_info['GPS_information']:
                    location = "未知位置"
                else:
                    location = GeoUtil.find_address_from_GPS(GPS_info['GPS_information']['GPSLatitude'], GPS_info['GPS_information']['GPSLongitude'])
            except Exception as e:
                print(file_path)
                traceback.print_exc()
                continue
            finally:
                pass

            new_path = os.path.join(photo_path, y)
            if (not os.path.exists(new_path)):
                os.mkdir(new_path)
            new_path = os.path.join(new_path, m + "-" + location)
            if (not os.path.exists(new_path)):
                print("创建", new_path)
                os.mkdir(new_path)
            new_file_path = os.path.join(new_path, item)

            # md5
            md5 = Md5Util.get_file_md5(file_path)
            if (md5_dict_t.has_key(md5)):
                continue
            else:
                md5_dict_t[md5] = file_path

            if os.path.exists(new_file_path):
                new_file_path = os.path.join(new_path, str(int(time.time())) + item)

            try:
                shutil.move(file_path, new_file_path)
            except Exception as e:
                print(file_path, new_file_path)
            else:
                pass
            finally:
                pass