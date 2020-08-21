# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/21 9:08 AM
@Author  : dengwei
@File    : main.py
'''

import os

if __name__ == "__main__":

    md5_dict_t = {}
    photo_path = "/Volumes/ntfs_dw/Photos"
    # photo_path = "/Users/dengwei/Downloads/pic"
    for root, dirs, files in os.walk("/Volumes/ntfs_dw/Photos1"):
        for item in files:
            file_path = os.path.join(root, item)
            # print file_path, os.path.isfile(file_path), getmd5(file_path)
            if not os.path.isfile(file_path):
                continue

            # 创建时间
            c_time = time.localtime(os.stat(file_path).st_birthtime)
            c_time_y = time.strftime('%Y', c_time)
            # 修改时间
            m_time = time.localtime(os.stat(file_path).st_mtime)
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
                GPS_info = find_GPS_image(pic_path=file_path)  # 照片
                location = find_address_from_GPS(GPS=GPS_info)
            except Exception as e:
                print file_path
                traceback.print_exc()
                continue
            else:
                location = "未知位置"
            finally:
                pass

            new_path = os.path.join(photo_path, y)
            if (not os.path.exists(new_path)):
                os.mkdir(new_path)
            new_path = os.path.join(new_path, m + "-" + location)
            if (not os.path.exists(new_path)):
                print "创建", new_path
                os.mkdir(new_path)
            new_file_path = os.path.join(new_path, item)

            # md5
            md5 = getmd5(file_path)
            if (md5_dict_t.has_key(md5)):
                continue
            else:
                md5_dict_t[md5] = file_path

            if os.path.exists(new_file_path):
                new_file_path = os.path.join(new_path, str(int(time.time())) + item)

            try:
                shutil.move(file_path, new_file_path)
            except Exception as e:
                print file_path, new_file_path
            else:
                pass
            finally:
                pass