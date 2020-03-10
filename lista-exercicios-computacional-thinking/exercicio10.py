distancia = int(input("Qual a distancia em metros"))
tempo = int(input("Qual o tempo em segundos"))

metros = int(1000)
segundosNaHora = int(60*60)

metrosPorSegundo = distancia / tempo
quilometrosPorHora = metrosPorSegundo * (segundosNaHora / metros)

print(str(metrosPorSegundo) + " metros por segundo")
print(str(quilometrosPorHora) + " quilometros por hora")