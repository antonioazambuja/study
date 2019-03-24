letra = input("digite uma letra: ")
vogais = ['A', 'E', 'I', 'O','U']
alfabeto_novog = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
if letra.upper() in vogais:
    print("vogal!")
elif letra.upper() in alfabeto_novog:
    print("consoante!")
else:
    print('não é letra!')
