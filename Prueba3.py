def is_float(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False
print(is_float('2.2.2'))
print(is_float('2.123'))

edad = "2.2.2"

if edad.isdigit():
    print("cadena es válida")
else:
    print("Cadena es no valida")