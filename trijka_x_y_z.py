def func_xyz(n):
    z = 0
    tr = []
    while len(tr) < n:
        z += 1
        for y in xrange(z):
            for x in xrange(y):
                if x**2 + y**2 == z**2:
                    tr.append((x,y,z))
                if len(tr) >= n:
                    break
            if len(tr) >= n:
                break
            
    return tr
print(func_xyz(5))
