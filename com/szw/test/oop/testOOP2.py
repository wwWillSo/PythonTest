#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: WillSo
@license: Apache Licence 
@file: testOOP2.py
@time: 2017\10\9 0009 16:20
"""

if __name__ == '__main__':
    pass

class Animal(object) :
    def run (self) :
        print('animal is running...')

class Dog(Animal) :
    def run (self) :
        print('Dog is running...')
class Cat(Animal) :
    def run (self) :
        print('Cat is running...')

#鸭子类型,只需要实现了run方法，不需要真正地继承
class Timer(object) :
    def run (self) :
        print('start...')

def run_twice(animal) :
    animal.run()
    animal.run()

# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()
run_twice(Dog())
run_twice(Cat())
run_twice(Timer())
print(Cat())