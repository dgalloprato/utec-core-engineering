#!/usr/bin/env python3
resultado = ""
for codigo in range(97, 123):
    letra = chr(codigo)
    if letra != "q" and letra != "e":
        resultado += letra
print(resultado)
