a, b, = 1, 1
while len(str(b)) < 1000:
    a, b = b, a + b

print (len(str(b)))
print (b)
