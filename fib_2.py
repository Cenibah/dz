a, b, k = 1, 1, 2
while k < 100000:
    a, b, k = b, a + b, k + 1

print (len(str(b)))
