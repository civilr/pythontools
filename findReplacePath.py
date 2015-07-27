# coding=utf-8
# 指定目录下的所有文件中的固定内容替换为新的内容。

import os

def replaceStr(f,str0,str1):
    lines =[]
    for line in f.readlines():
        line = line.replace(str0,str1)
        lines.append(line)
    f.close()
    return lines

def writeStr(f,lines):
    for line in lines:
        f.write(line)
    f.close()

inputpath=raw_input('in put the path you want :')

inputstr0=raw_input('in put the str you want replace :')

inputstr1=raw_input('in put the str you want replaced :')

files = os.listdir(inputpath)

for f in files:
    if (os.path.isfile(inputpath+'/'+f)):
        instance = open(inputpath+'/'+f)
        lines = replaceStr(instance,inputstr0,inputstr1)
        instance_w = open(inputpath+'/'+f,'w')
        writeStr(instance_w,lines)
