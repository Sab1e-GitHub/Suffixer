#!/usr/bin/env python3

import os

countTotal = 0
countSuccess = 0
countFail = 0

#修改文件后缀
def editFileSuffix():
    global countTotal 
    global countSuccess 
    global countFail
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename=os.path.join(path, file_name)
            print("@Suffixer:找到文件:"+filename)
            countTotal+=1
            if filename.endswith(suffix):
                countSuccess+=1
                print("@Suffixer:正在修改，原文件名:"+filename)
                newFilename = filename.split(".bc!")[0]
                print("@Suffixer:新文件名:"+newFilename)
                os.rename(filename, newFilename)
            else:
                countFail+=1
                print("@Suffixer:不是"+suffix+"后缀的文件")
    result()

def deleteSuffixFile():
    global countTotal 
    global countSuccess 
    global countFail
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename=os.path.join(path, file_name)
            print("@Suffixer:找到文件:"+filename)
            countTotal+=1
            if filename.endswith(suffix):
                countSuccess+=1
                print("@Suffixer:正在删除:"+filename)
                os.remove(filename)
            else:
                countFail+=1
                print("@Suffixer:不是"+suffix+"后缀的文件")
    result()
#start

def result():
    global countTotal 
    global countSuccess 
    global countFail
    print("\n============RESULT============\n")
    print("共计找到文件："+str(countTotal))
    print("操作成功文件："+str(countSuccess))
    print("操作失败文件："+str(countFail))
    print("\n============RESULT============\n")

print("\n============SUFFIXER============\n")
print("欢迎使用Suffixer\n作者:Sab1e")
print("\n============SUFFIXER============\n")
suffix = input("请输入文件后缀:")

inputPath = input("请输入文件所在的文件夹(回车则默认为本程序所在的目录):")
if(inputPath==""):
    paths = os.walk(r"./")
else:
    inputPath = r"+inputPath+"
    paths = os.walk(inputPath)
#os.walk(r"./")

while(1):
    countTotal = 0
    countSuccess = 0
    countFail = 0
    selection = input("请输入选项(0=去除文件后缀"+suffix+",1=删除"+suffix+"后缀的文件,2=退出程序)")
    if(selection=="0"):
        editFileSuffix()
    elif(selection=="1"):
        deleteSuffixFile()
    elif(selection=="2"):
        exit()
    else:
        print("输入不合法！")
