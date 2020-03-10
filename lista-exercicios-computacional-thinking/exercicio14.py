valorAVista = int(input("valor a vista"))
valorParcela = int(input("valor parcela"))

valorAPrazo = valorParcela * 10

valorPercDesconto = (valorAPrazo / valorAVista - 1) * 100

print(str(valorPercDesconto))    