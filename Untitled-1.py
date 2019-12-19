import requests
import time
import datetime
import hashlib

url = "https://app.netease.im/nimApi/bill/overview"
t = time.time()

timestamp = int(round(t * 1000))
payload = "monthDate=2019-10&entId=23714"

hl = hashlib.md5()
checksum = hashlib.md5(bytearray(payload+"timestamp="+str(timestamp))).hexdigest()

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'channel': "ypp",
    'checksum': checksum,
    'timestamp': timestamp,
    }

response = requests.request("POST", url, data=payload, headers=headers)
#ret = requests.post(url, headers=header, data=param_data)