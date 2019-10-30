def EvenChecker(a):
    if a % 2 == 0:
        if a % 4 == 0:
            print("Ta liczba jest wielokrotnością 4!")
        else:
            print("Ta liczba jest parzysta!")
    else:
        print("Ta liczba jest nieparzysta!")
def DivideChecker(num1, num2):
    if num1 % num2 == 0:
        print("Num1 jest podzielne przez num2!")
    else:
        print("Num1 nie jest podzielne przez num2!")
while True:
    try:
        a = int(input("Podaj liczbę całkowitą: "))
        break
    except ValueError:
        print("Ups! To nie jest liczba całkowita. Spróbuj ponownie...")
EvenChecker(a)
while True:
    try:
        num1 = int(input("Podaj liczbę całkowitą dla num1: "))
        break
    except ValueError:
        print("Ups! To nie jest liczba całkowita. Spróbuj ponownie...")
while True:
    try:
        num2 = int(input("Podaj liczbę całkowitą dla num2: "))
        break
    except ValueError:
        print("Ups! To nie jest liczba całkowita. Spróbuj ponownie...")
DivideChecker(num1, num2)