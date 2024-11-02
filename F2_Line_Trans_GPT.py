"""
该py文件，将会被封装为.exe文件，用于在Windows下，
一键运行main.py文件。
从而实现解耦，不需要每次更改配置后，都重新编译一个exe文件。
"""

import os

# 运行 main.py 文件
os.system('python D:\programfiles\F2_Line_translation_based_GPT_API\main.py')
