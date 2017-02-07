# -*- coding:utf-8 -*-
import string
import StringIO

str="ni       hao"
print str.split()
#StringIO可以作为一个内存文件对象
s=StringIO.StringIO()
s.write("aaaa")
lines=['xxxxx','bbbbb']
s.writelines(lines)
s.seek(0)
print s.read()

print s.getvalue()
s.write("tttttt")
s.seek(0)
print s.readlines()
print s.len

