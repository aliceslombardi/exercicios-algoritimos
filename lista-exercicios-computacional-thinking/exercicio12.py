rmAluno = int(input("Digiete seu RM"))

digito1 = int(rmAluno % 10)
digito2 = int( (rmAluno % 100) / 10)
digito3 = int( (rmAluno % 1000) / 100)
digito4 = int( (rmAluno % 10000) / 1000)
digito5 = int( (rmAluno % 100000) / 10000)

soma = digito1 + digito2 + digito3 + digito4 + digito5

print(str(soma) + " = " + str(digito5) + " + " + str(digito4) + " + " + str(digito3) + " + " + str(digito2) + " + " + str(digito1))