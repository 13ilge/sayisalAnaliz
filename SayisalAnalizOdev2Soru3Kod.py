x = 2

for i in range(1, 5):
    fx = 4 * (2.71**(-0.5 * x)) - x

    print(f"Iterasyon {i}:")
    print(f"x0 = {x}")
    print(f"f(x0) = {fx}")

    trv = -2 * (2.71**(-0.5 * x)) - 1

    x = x - fx / trv

    print(f"Yeni x: {x}\n")

print(f"Son Kök Yaklaşımı: {x}")