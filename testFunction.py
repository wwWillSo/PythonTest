def enroll (name, gender, age=20, city='GZ') :
    print('name : ', name)
    print('gender : ', gender)
    print('age : ', age)
    print('city : ', city)
enroll('WillSo', 'male', city='SZ')

def add_END(L=[]) :
    if len(L) == 0 :
      L.append('END')
    return L
print(add_END())
print(add_END())
print(add_END())

#可变参数用法
def cal(*numbers) :
    sum = 0
    for n in numbers :
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print(cal(*nums))
print(cal(1,2,3))

#关键字参数用法
def enroll2(name, gender, age=20, city='GZ', **other) :
    print('name : ', name)
    print('gender : ', gender)
    print('age : ', age)
    print('city : ', city)
    print('hobbits : ', other)
enroll2('WillSo', 'male', hobbits='basketball', city='SZ',fav='sleep')

#命名关键字参数用法
def enroll3(name, gender, age=20, *, city='GZ', province) :
    print('name : ', name)
    print('gender : ', gender)
    print('age : ', age)
    print('city : ', city)
    print('province : ', province)
enroll3('WillSo', 'male', province = 'GD')

#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2 , c=3)
f1(1, 2, 3, 4, 5, 6, 7, 8, x=100, y=1000)
f2(1, 2, 3, d=4, x=100, y=1000)

args=(1, 2, 3, 4)
f1(1, 2, *args)

#递归
def fact(n) :
    if  n == 1 :
        return 1
    return n * fact(n-1)
print(fact(5))