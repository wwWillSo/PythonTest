def sum1 (start, end) :
    total = 0
    for x in range(start, end + 1) :
        total += x
    return total
print(sum1(1, 100))

def sum2 (start, end) :
    total = 0
    for x in range(start, end + 1) :
        total += x * x + 1
    return total
print (sum2(1, 100))

#由于上面两个函数都涉及到累加，所以可以基于累加的操作将上面两个函数对x的操作抽象出来
def sum (start, end, handle) :
    total = 0
    for x in range(start, end + 1) :
        total += handle(x)
    return total
def identity(n) :
    return n
def square_plus_one(n) :
    return n ** 2 + 1
print(sum(1, 100, identity))
print(sum(1, 100, square_plus_one))
