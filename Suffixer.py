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
            print("找到文件:"+filename)
            countTotal+=1
            if filename.endswith(suffix):
                countSuccess+=1
                print("正在修改，原文件名:"+filename)
                newFilename = filename.split(".bc!")[0]
                print("新文件名:"+newFilename)
                os.rename(filename, newFilename)
            else:
                countFail+=1
                print("不是"+suffix+"后缀的文件")
    result()

def deleteSuffixFile():
    global countTotal 
    global countSuccess 
    global countFail
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename=os.path.join(path, file_name)
            print("找到文件:"+filename)
            countTotal+=1
            if filename.endswith(suffix):
                countSuccess+=1
                print("正在删除:"+filename)
                os.remove(filename)
            else:
                countFail+=1
                print("不是"+suffix+"后缀的文件")
    result()

def listFilesWithSuffix():
    global countTotal 
    global countSuccess 
    global countFail
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename=os.path.join(path, file_name)
            if filename.endswith(suffix):
                print("找到后缀名文件:"+filename)
                countSuccess+=1
            countTotal+=1
    print(f"\n共找到{countSuccess}个后缀名为{suffix}的文件")

def result():
    global countTotal 
    global countSuccess 
    global countFail
    print("\n============RESULT============\n")
    print("共计找到文件："+str(countTotal))
    print("操作成功文件："+str(countSuccess))
    print("操作失败文件："+str(countFail))
    print("\n==============================\n")

print("\n============SUFFIXER============\n")
print("欢迎使用Suffixer\n作者:Sab1e")
print("\n================================\n")
suffix = input("请输入文件后缀(例如：.7z .html .png):")

inputPath = input("请输入文件所在的文件夹(回车则默认为本程序所在的目录):")
if(inputPath==""):
    paths = os.walk(r"./")
else:
    inputPath = r"+inputPath+"
    paths = os.walk(inputPath)

while(1):
    countTotal = 0
    countSuccess = 0
    countFail = 0
    print("\n============SUFFIXER============\n")
    print(f"0=去除文件后缀{suffix}")
    print(f"1=删除{suffix}后缀的文件")
    print(f"2=列出所有后缀名为{suffix}的文件")
    print(f"3=退出程序")
    print("\n================================\n")
    selection = input("请输入选项:")
    if(selection=="0"):
        editFileSuffix()
    elif(selection=="1"):
        deleteSuffixFile()
    elif(selection=="2"):
        listFilesWithSuffix()
    elif(selection=="3"):
        exit()
    else:
        print("输入不合法！")
