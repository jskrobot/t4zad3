x = 2354
def wyznaczanie_cyfr():
    j = x % 10
    print(j)
    d = int((x / 10) % 10)
    print(d)
    s = int((x / 100) % 10)
    print(s)


if x > 99:
    print("poprawna liczba")
    wyznaczanie_cyfr()
else:
    print("bledna liczba")
