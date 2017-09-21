classmates = ['1', '2', '3']
print(classmates.__getitem__(0))
print(len(classmates))
print(classmates[-1])

classmates.append('willso')
print(classmates)
classmates.pop(2)
print(classmates)
classmates[0] = 'helloworld'
print(classmates)
p = ['22', '3']
classmates[1] = p
print(classmates)
print(len(classmates))