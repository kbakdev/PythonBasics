#12. Sprawdź czy liczba wprowadzona jest podzielna
#przez 3 lub 5.

number = int(input('Input number: '))

if number%3==0 or number%5==0:
    print('The number is divisible by 3 or 5.')
else:
    print("The number isn't divisible by 3 or 5.")