
num = 100
run = True
while run:
    guess = int(raw_input('Vvedit chuslo '))
    if guess == num:
        print('Vu vhadalu chuslo')
        run = False
    elif guess < num:
        print('vvedene chuslo bilshe')
    else:
        print('vvedene chuslo menshe')
else:
    print(guess)
 
