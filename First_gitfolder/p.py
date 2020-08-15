#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv   # argv参数用列表存储命令行的所有参数
    if len(args)==1:  # 当列表长度为1时即只有一个参数时
        print('Hello, world!')
    elif len(args)==2: # 当命令行有两个参数时
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
    