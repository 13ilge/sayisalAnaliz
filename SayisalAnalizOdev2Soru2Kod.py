a = 1
b = 2

for i in range(1, 5):
    c = (a + b) / 2
    fa = a**3 + 4*a**2 - 10
    fc = c**3 + 4*c**2 - 10

    print(f"Iterasyon {i}:")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"{fa}   {fc}")

    if fa * fc < 0:
        b = c
    else:
        a = c

    hata = (b - a) / 2
    print(f"Hata {hata}\n")

kok = (a + b) / 2
print(kok)