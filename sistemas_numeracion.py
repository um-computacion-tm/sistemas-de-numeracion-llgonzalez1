def decimal_binario(decimal):
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return int (binario)
print (decimal_binario(10))
