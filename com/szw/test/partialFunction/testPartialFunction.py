#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: WillSo
@license: Apache Licence 
@file: testPartialFunction.py
@time: 2017\10\9 0009 15:55
"""

import functools
int2 = functools.partial(int, base=2)
i = int2('10', base=2)
print(i)