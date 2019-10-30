import random
def checker():
    i = 0
    a = random.randrange(1, 11, 1)
    while True:
        b = input("Zgadnij liczbę od 1 do 10, jeśli chcesz wyjść napisz exit: ")
        if b=="exit":
            print("Koniec!")
            break
        else:
            b = int(b)
            if a > b:
                i += 1
                print("Za mało!")
            elif a < b:
                i += 1
                print("Za dużo!")
            else:
                i += 1
                print("Brawo! Wylosowana liczba to {}, liczba prób to {}".format(a, i))
                break
checker()