#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: WillSo
@license: Apache Licence 
@file: slots.py
@time: 2017\10\10 0010 14:16
"""

class Student(object) :
    __slots__ = ['name', 'score']
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def set_name(self, name):
        self.name = name
    def get_name(self):
        print(self.name)
    def set_score(self, score):
        self.score = score
    def get_score(self):
        print(self.score)
    def print_all(self):
        self.get_name()
        self.get_score()

stu = Student('willso', score = 3)
stu.set_name('WillSo')
stu.print_all()

if __name__ == '__main__':
    pass