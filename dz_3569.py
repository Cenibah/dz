i = 1
num = []
while len(num) < 100:
        i += 1
        #if i % 3 == 0 and i % 5 == 0:
        #        continue
        #if i % 3 == 0 or i % 5 == 0:
        #        num.append(i)
        if (i % 3 == 0) != (i % 5 == 0):
                num.append(i)

                
print(num)

     
 
