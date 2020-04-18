# 19. Napisz program, która sprawdza czy dana liczba
# jest liczbą pierwszą.

p = int(input('Input number: '))
x = 2
if x<=p:
    if x/p:
        print('work')
        print(1)
    else:
        print('not working')
        print(2)
        print(x = x+1)
else:
    print('not working')
    print(3)