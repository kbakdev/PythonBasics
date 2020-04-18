# Napisz program, który odczytuje wyraz i sprawdza
# czy wprowadzony wyraz to Akademia.

word = input('Input word: ')
# Akademia

if word.lower()=="akademia":
    print('Valid password')
else:
    print('Invalid password')