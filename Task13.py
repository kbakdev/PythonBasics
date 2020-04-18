# Odczytaj wiek osoby i sprawdź czy osoba jest
# pełnoletnia czy niepełnoletnia.

age = int(input('Input age: '))

if age<=17:
    print('This person is a minor.')
else:
    print('This person is of legal age.')