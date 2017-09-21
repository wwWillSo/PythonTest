#分片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[::3])

#迭代
for l in L :
    print(l)

d = {'a': 1, 'b': 2, 'c': 3}
for x in d :
    print(x ,' : ', d[x])

#列表生成式
print(list(range(1, 11)))
print([x * x for x in range(1, 11) if x % 2 ==0])

print([x + y for x in 'ABC' for y in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d2 = {'a': '1', 'b': '2', 'c': '3'}
for x, y in d2.items() :
    print(x, ' : ', y)
print([k + ':' + v for k, v in d2.items()])

#生成器
L =[x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
for n in g :
    print(n)