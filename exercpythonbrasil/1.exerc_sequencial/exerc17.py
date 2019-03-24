# entrada de dados em float
metros = float(input("Qtd de metros que sera pintada: "))
# litros a serem usados para pintar a qtd informada 
litros = metros / 6
# calculo de latas e preço
latas = (litros // 18) + 1
custo_lata = latas * 80
print("Apenas latas de 18 litros:",latas,"lata, R$",custo_lata,".")
# calculo de galões e preço
galao = (litros // 3.6) + 1
custo_galao = galao * 25
print("Apenas galões de 3.6 litros:",galao,"galão, R$",custo_galao,".")
# variaveis a serem usadas a seguir
menor_custo = 0
custo_final = 0
latas_menor = 0
galao_menor = 0
litros_final = 0
# testando o menor custo para servir de parametro
if custo_lata < menor_custo:
    menor_custo = custo_lata
else:
    menor_custo = custo_galao
# soma a qtd de latas e galões para a mistura ser o menor custo
while litros_final < litros:
    if litros_final < litros:
        custo_final += 80
        litros_final += 18
        latas_menor = latas_menor + 1
    if litros_final < litros:
        custo_final += 25
        litros_final += 3.6
        galao_menor = galao_menor + 1
# diminuindo o percentual de 10% sobre o valor final da mistura
if galao_menor + latas_menor > 1:
    percent_final = custo_final * 0.1
    custo_final -= percent_final
# imprimindo o valor e a qtd da mistura se for menor que o menor custo
if custo_final <= menor_custo:
    print("Qtd de latas:",latas_menor,"Qtd de galões:",galao_menor,"Custo da mistura: R$",custo_final,".")
