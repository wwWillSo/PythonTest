#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: WillSo
@license: Apache Licence 
@file: property.py
@time: 2017\10\10 0010 15:07
"""

class Student(object):

    # def get_score(self):
    #      return self._score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def age (self) :
        return 100-self._score

stu = Student()
stu.score = 80


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print('%s/%s' % (self._path, path))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

if __name__ == '__main__':
    pass