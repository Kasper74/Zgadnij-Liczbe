import random

prawidlowa_liczba = random.randint(1, 100)
liczba = 0

while liczba != prawidlowa_liczba:

  liczba = int(input("Podaj Liczbę: "))

  if liczba > prawidlowa_liczba:
    print("Twoja liczba jest większa od prawidłowej")
    print("Podaj mniejszą liczbę")

  elif liczba < prawidlowa_liczba:
    print ("Twoja liczba jest mniejsza od prawidłowej")
    print("Podaj większą liczbę")

  else:
    print("Udało Ci się zgadnąć!")
