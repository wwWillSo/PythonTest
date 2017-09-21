#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: WillSo
@license: Apache Licence 
@file: TestDecorator.py
@time: 2017\9\30 0030 16:01
"""

import datetime
import functools

def log(func) :
    @functools.wraps(func)
    def wrapper(*args, **kw) :
        print('call %s() : ' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log2(text) :
    def decorator(func) :
        @functools.wraps(func)
        def wrapper(*args, **kw) :
            print('%s %s() : ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('exec')
def now() :
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
f = now
f()
print(now.__name__)
print(f.__name__)
