#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 根据传入的文件夹地址遍历下面的js文件，生成统一导出的index.js，需要注意的是重名的模块

# 获取目录下文件
import os


file_name_list = []
file_rel_path_dict = {}


def handle_dir(path):
    if os.path.isdir(path):
        dir_files = os.listdir(path)
        for dir_file in dir_files:
            handle_dir(os.path.join(path, dir_file))
    else:
        # 获取对应的相对路径 记录到列表中
        file_name = os.path.basename(path).rstrip('.js')
        file_rel_path_dict[file_name] = os.path.relpath(path, os.getcwd())
        # 获取基本文件名 记录到列表中
        file_name_list.append(file_name)


write_lines = []


def create_index_js_file():
    # 引入
    for file_name in file_name_list:
        write_lines.append('const {} = require(\'./{}\');\n'.format(file_name,file_rel_path_dict[file_name]))

    write_lines.append('\n')
    write_lines.append('module.exports = {\n')
    # 导出
    write_lines.append(','.join(file_name_list))
    write_lines.append('\n}')
    fo = open(os.path.join(os.getcwd(), "index_new.js"), "w")
    fo.writelines(write_lines)
    # 关闭文件
    fo.close()


dir_path = input('please input dir path: ')
# dir_path = './lib'
dir_path = os.path.abspath(dir_path)
if os.path.isdir(dir_path):
    handle_dir(dir_path)
    create_index_js_file()
else:
    print('please input dir!')
