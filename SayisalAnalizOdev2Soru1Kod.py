a = 2
b = 4
for i in range(1, 5):
    c = (a + b) / 2
    fa = a**3 - 2*a**2 - 5
    fc = c**3 - 2*c**2 - 5
    print(f"Iterasyon {i}:")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"{fa}  {fc}")
    if fa * fc < 0:
        b = c
    else:
        a = c
kok = (a + b) / 2
print(kok)