#!/usr/bin/env python3

def safe_print_division(a, b):
    resultado = None

    try:
        resultado = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(resultado))

    return resultado
