#!/usr/bin/env python3

resultado = ""

for codigo in range(97, 123):
    letra = chr(codigo)
    if letra != "e" and letra != "q":
        resultado += letra

print("{}".format(resultado), end=""))
