#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'WillSo'

class Student(object) :
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_name_score(self):
        print('%s : %s' % (self.name, self.score))
    def print_grade(self):
        if self.score >= 90 :
            return '优'
        else :
            return '良'

bart = Student('Bart Thompson', 90)
print(bart.name)
print(bart.score)
bart.print_name_score()
bart.print_grade()
# bart.name = 'Bart Thompson'
# print(bart.name)