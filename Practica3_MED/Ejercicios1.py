meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

numero = int(input("Ingrese un número del 1 al 12: "))

if numero >= 1 and numero <= 12:
    mes = meses[numero - 1]
    print("El mes correspondiente al número", numero, "es", mes)
else:
    print("Número inválido. Por favor, ingrese un número del 1 al 12.")
