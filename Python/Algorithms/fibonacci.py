"""packing vs unpacking"""

def fibonacci1(n):
    a = 0
    b = 1
    while a < n: 
        yield a
        future = a + b
        a = b
        b = future

def fibonacci2(n):
    a, b = 0, 1
    while  a < n:
        yield a
        a, b = b, a + b


for i in fibonacci1(100):
    print("{0}, ".format(i), end='')

print()

for i in fibonacci2(100):
    print("{0}, ".format(i), end='')
