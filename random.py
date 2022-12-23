import random
a = random.randint(0, 9)
b = random.randint(0, 9)
print(a)
print(b)
if(a < b):
    a, b = b, a
    print(a)
    print(b)
c = a-b
print(c)
