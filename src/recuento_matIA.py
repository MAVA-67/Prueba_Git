# Datos inventados de una bandeja; cada elemento es un instrumento.
instrumentos = ["pinza", "tijera", "pinza"]
esperadas = 2
observadas = 0

# Recorremos la lista, elemento a elemento.
for instrumento in instrumentos:
    if instrumento == "pinza":
        observadas = observadas + 1

print("Pinzas esperadas:", esperadas)
print("Pinzas observadas:", observadas)

# Comparamos el recuento con lo esperado.
if observadas < esperadas:
    print("Resultado: faltan pinzas")
elif observadas > esperadas:
    print("Resultado: sobran pinzas")
else:
    print("Resultado: coincide")
