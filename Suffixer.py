#!/usr/bin/env python3

import os

def get_paths(input_path):
    if input_path == "":
        return os.walk(r"./")
    else:
        return os.walk(input_path)

# 修改文件后缀
def edit_file_suffix(paths, suffix):
    count_total = 0
    count_success = 0
    count_fail = 0
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename = os.path.join(path, file_name)
            count_total += 1
            if filename.endswith(suffix):
                new_filename = filename[:-len(suffix)]
                try:
                    os.rename(filename, new_filename)
                    count_success += 1
                    print(f"修改成功: {filename} -> {new_filename}")
                except Exception as e:
                    count_fail += 1
                    print(f"修改失败: {filename}, 错误: {e}")
            else:
                count_fail += 1
                print(f"跳过: {filename}, 不是后缀 {suffix} 的文件")
    result(count_total, count_success, count_fail)

def delete_suffix_file(paths, suffix):
    count_total = 0
    count_success = 0
    count_fail = 0
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename = os.path.join(path, file_name)
            count_total += 1
            if filename.endswith(suffix):
                try:
                    os.remove(filename)
                    count_success += 1
                    print(f"删除成功: {filename}")
                except Exception as e:
                    count_fail += 1
                    print(f"删除失败: {filename}, 错误: {e}")
            else:
                count_fail += 1
                print(f"跳过: {filename}, 不是后缀 {suffix} 的文件")
    result(count_total, count_success, count_fail)

def list_files_with_suffix(paths, suffix):
    count_total = 0
    count_success = 0
    for path, dir_lst, file_lst in paths:
        for file_name in file_lst:
            filename = os.path.join(path, file_name)
            count_total += 1
            if filename.endswith(suffix):
                count_success += 1
                print(f"找到后缀名文件: {filename}")
    print(f"\n共找到 {count_success} 个后缀名为 {suffix} 的文件")

def result(count_total, count_success, count_fail):
    print("\n============RESULT============\n")
    print(f"共计找到文件：{count_total}")
    print(f"操作成功文件：{count_success}")
    print(f"操作失败文件：{count_fail}")
    print("\n==============================\n")

def main():
    print("\n============SUFFIXER============\n")
    print("欢迎使用Suffixer\n作者:Sab1e")
    print("\n================================\n")

    suffix = input("请输入文件后缀(例如：.7z .html .png):")

    input_path = input("请输入文件所在的文件夹(回车则默认为当前目录):")

    while True:
        paths = get_paths(input_path)

        print("\n============SUFFIXER============\n")
        print(f"0=去除文件后缀 {suffix}")
        print(f"1=删除 {suffix} 后缀的文件")
        print(f"2=列出所有后缀名为 {suffix} 的文件")
        print(f"3=退出程序")
        print("\n================================\n")
        selection = input("请输入选项:")
        if selection == "0":
            edit_file_suffix(paths, suffix)
        elif selection == "1":
            delete_suffix_file(paths, suffix)
        elif selection == "2":
            list_files_with_suffix(paths, suffix)
        elif selection == "3":
            exit()
        else:
            print("输入不合法！")

if __name__ == "__main__":
    main()
