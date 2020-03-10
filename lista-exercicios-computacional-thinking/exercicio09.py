vlProduto = int(input("Qual o valor do produto"))
Desconto = int(input("Qual o percentual de Desconto"))

vlDesconto = vlProduto * (Desconto/100)

comDesconto = vlProduto - vlDesconto
comAcrecimo = vlProduto + vlDesconto

print("valor com desconto= " + str(comDesconto) + ", valor com acrecimos=" + str(comAcrecimo))