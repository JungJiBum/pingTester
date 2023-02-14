from datetime import datetime
import logging
import subprocess
from debugpy import log_to

log_today = datetime.now()
today_all = log_today
log_today = str(log_today).split(" ")[0]

path = r"절대경로"
# 2022-03-28.log
log = logging.getLogger(path+str(log_today)+".log")
log.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(path+str(log_today)+".log")
streamHandler = logging.StreamHandler()

log.addHandler(fileHandler)
log.addHandler(streamHandler)


key = ['장비명']

value = ['아이피']
dict = {name: value for name, value in zip(key, value)}

# ping 커맨드 돌리하는 함수


def check(ip):
    param = '-n'
    command = ['ping', param, '1', ip]
    response = subprocess.call(command)

    if response == 0:
        return "통신 양호"
    else:
        return "네트워크 이상"


val_rs = {}
for k, v in dict.items():
    val_rs[k] = check(v)

ip = []
for key, value in val_rs.items():
    if value == "네트워크 이상":
        ip.append(key)

for i in ip:
    if dict.get(i):
        if val_rs.get(i):
            log.info("일자 : {}, 장비명 : {}, IP : {}, 상태 : {}".format(
                today_all, i, dict.get(i), val_rs.get(i)))
