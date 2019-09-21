# -*- coding: utf-8 -*- 
# @Author : yunze
import pandas as pd
data = pd.read_excel(r'E:\python project\analyze\就业情况数据.xls')
guangdong_sum = 0
other_sum = 1
site = data['生源地']
for i in site:
    if i.startswith('广东省'):
        guangdong_sum += 1
    else:
        other_sum += 1
print(guangdong_sum)
print("------------------")
print(other_sum)

print("---------")
print(guangdong_sum+other_sum)
