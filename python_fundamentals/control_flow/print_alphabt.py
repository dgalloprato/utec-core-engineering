#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for letter in alphabet:
    if letter != "e" and letter != "q":
        result += letter

print(result)
