metros = int(input("Informe a qtd em metros quadrados: "))
litros = metros / 3
if litros <= 18:
	print("1 lata, custando R$ 80")
else:
	latas = (litros // 18) + 1
	custo = latas * 80
	print(latas,"latas, custando R$",custo)	
    