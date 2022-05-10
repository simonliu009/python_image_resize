#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /Users/simonliu/Documents/python/imgresize.py
# Project: /Users/simonliu/Documents/python
# Created Date: 2022-05-05 23:00:44
# Author: Simon Liu
# -----
# Last Modified: 2022-05-10 14:35:29
# Modified By: Simon Liu
# -----
# Copyright (c) 2022 SimonLiu Inc.
# 
# 将文件夹下的图片居中剪裁为指定比例并缩放到指定大小
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###

from PIL import Image
from pathlib import Path
import time

cnt = 0
display_each_line = 10
src_dir = input('请输入图片文件夹位置：')
if src_dir[0]=='~':
    src_dir=src_dir.replace('~',str(Path.home()))
    print('图片文件夹:',src_dir)
src_path = Path(src_dir)

if(not src_path.exists()):
    print(f'文件夹{src_dir}不存在，请检查输入的文件夹名称是否正确。')

# file_list = src_path.iterdir()
file_list = src_path.glob('*.jp*g')

# 源文件夹检查.DS_Store文件
target = src_path/'.DS_Store'
print('检查 .DS_Store 文件是否存在')
if (target.exists()):
    Path.unlink(target)
    print(f'{target} 文件已自动删除。')
else:
    print(f'.DS_Store 文件不存在，继续操作。')
    
line_count = 0
dir_list = []
for f in sorted(file_list, key = lambda f : f.stem):
    # 目标文件夹检查.DS_Store文件
    if(f.name=='.DS_Store'):
        print('!!! === 发现 .DS_Store文件，已删除 === !!!')
        Path.unlink(f)
    elif f.is_file():
    # else:
        cnt += 1
        if cnt%display_each_line == 1:
            line_count += 1
            print('\n%d | %15s'%(line_count,f.name),end='')
        else:
            print('%15s'%f.name,end='')
    elif f.is_dir():
        dir_list.append(f)
    else:
        print('无法识别的类型：',str(f))

if dir_list:
    print('\n目标文件夹发现如下子文件夹。请检查：')
    for dir in dir_list:
        print('%15s'%(str(dir)))

