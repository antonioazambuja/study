size = float(input("Informe o tamanho do arquivo para download:(MB) "))
speed = float(input("Informe o velocidade do link da internet:(Mbps) "))

time = (size / speed) / 60
print("Tempo esperado:",time,"Min.")
