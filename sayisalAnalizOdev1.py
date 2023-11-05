import math

x=math.pi/5 

def taylorHesapFonk(x, n):
    depo=0
    for i in range(n):
        taylorFonk = ((-1)**i)*(x**(2*i))/math.factorial(2*i)
        depo = depo+taylorFonk
    return depo

cosx= math.cos(x)
n=1
tekTerimli=taylorHesapFonk(x,n)
n=2
ikiTerimli=taylorHesapFonk(x,n)

kesmeHatasi1=(cosx-tekTerimli)
kesmeHatasi2=(cosx-ikiTerimli)

print(f"tek terimde taylor {tekTerimli}")
print(f"iki terimde taylor {ikiTerimli}")
print(f"tek terimde kesme hatasi {kesmeHatasi1}")
print(f"iki terimde kesme hatasi {kesmeHatasi2}")