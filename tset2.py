# -*- coding:utf-8 -*-
s='窗 前 明 月 光'
print s
f=open('te.txt','w')
f.write(s)
f=open('te.txt','r')
words=f.readlines()[0].strip()
print words
print words.decode('utf-8')