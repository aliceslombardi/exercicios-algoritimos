salarioAntes = int(input("Qual o salario atual"))
salarioDepois = int(input("Qual o salario atualizado"))

valorPercentual = (salarioDepois / salarioAntes - 1) * 100

print(str(valorPercentual) + " % Porcento de aumento.")