#高阶函数
def add(x, y, f) :
    return f(x) + f(y)
print(add(-1, -3, abs))

#map
def f(x) :
    return x * x
L = list(range(1, 11))
result = map(f, L)
print(list(result))

def toString(number) :
    return str(number)
L = list(range(1,11))
result = map(toString, L)
print(list(result))

#reduce
from functools import reduce
def add2(x, y):
    return x + y
print(reduce(add2, [1, 2, 3, 4]))

def fn (x, y) :
    return x * 10 + y
def char2num(s) :
    return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}[s]
print(list(map(char2num, '12345')))
print(reduce(fn, map(char2num, '12345')))

#上面的fn和char2num可以合并在一个函数之内
def str2num(s) :
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}[s]
    return reduce(fn, map(char2num, s))
print(str2num('12345'))

#上面的操作还能用lambda简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}[s]
def str2int(s):
    return reduce(lambda  x, y : x * 10 + y,map(char2num, s))
print(str2int('12345'))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name) :
    return str(name).capitalize()
print(list(map(normalize, ['wwW', 'aAa'])))
print(list(map(lambda name : str(name).capitalize(), ['wilLso', 'micHAel'])))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L) :
    return reduce(lambda x, y : x * y, L)
print(prod([1,2,3,4,5]))