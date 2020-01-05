#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
import requests, time, hashlib


def post_nim_api(url, channel, param_dict):
    timestamp = str(int(time.time()))
    param_pair_list = []
    for name, val in param_dict.items():
        param_pair_list.append(name + "=" + str(val))

    param_pair_list.sort()
    param_data = "&".join(param_pair_list)
    checksum = hashlib.md5(bytearray(param_data + "&timestamp=" + timestamp, "utf-8")).hexdigest()
    header = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        "channel": channel,
        "timestamp": timestamp,
        "checksum": checksum
    }
    ret = requests.post(url, headers=header, data=param_data)
    return ret


if __name__ == '__main__':
    print(post_nim_api("https://app.netease.im/nimApi/bill/overview", "ypp",
                       {"entId": 23714, "monthDate": "2019-12"}).json())
