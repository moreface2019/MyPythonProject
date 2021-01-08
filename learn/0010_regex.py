# -*- coding: utf-8 -*-
import re

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>正则表达式 re>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print('用\d可以匹配一个数字，\w可以匹配一个字母或数字，.可以匹配任意字符')
print('用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符')
print()

print('要做更精确地匹配，可以用[]表示范围')
print('A|B可以匹配A或B')
print('^表示行的开头，^\d表示必须以数字开头')
print('$表示行的结束，\d$表示必须以数字结束')
print()

print('Python提供re模块，包含所有正则表达式的功能')
print('正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）')
print()

print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))
# >>>010 12345

t = '19:05:30'
print('Test:', t)
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.groups())
# >>>('19', '05', '30')