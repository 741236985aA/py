'''
name:the score panel.py
description:it can give your result row level
author:Zhengjialu
date:2022/6/23
update:2022/6/23
version:1.0.0
'''

result = float(input('please enter your result :'))

if 100 >= result >= 90:
    print('A')
elif 90 > result >= 80:
    print('B')
elif 80 > result >= 70:
    print('C')
elif 70 > result >= 60:
    print('D')
elif 60 > result >= 0:
    print('E')
else:
    print('error')
