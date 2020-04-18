# 18. Napisz program, który symuluje działanie słownika
# polsko-angielskiego. Użytkownik podaje słowo po
# Polsku i w odpowiedzi otrzymuje słowo po angielsku.

Dict = {"keyboard":"klawiatura", "mouse":"myszka", "chicken":"kurczak", "drewno":"wood"}

word = input(str("Input word: "))
print(Dict[word])