#创建数据文件
# 1. 需要文件名以抓取的对象和时间命名
# 2. 时间要精确到秒级别

import json
import datetime
import time

numbers=[2,3,4,5,6]

t = time.strptime('2016-05-09 21:09:30', '%Y-%m-%d %H:%M:%S')


print(t)

#filename='number.json'
#with open(filename,'w') as f_obj:
#    json.dump(numbers,f_obj)
