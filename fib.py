a, b, = 1, 1
while b < 10000000:
    a, b = b, a + b

print b
