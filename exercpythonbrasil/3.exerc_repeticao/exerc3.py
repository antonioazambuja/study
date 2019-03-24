def erro_nome():
    print("\nnome deve ter 3 ou mais caracteres!\n")


def erro_idade():
    print("\nidade deve ser entre 0 e 150!\n")


def erro_salario():
    print("\nsalario cadastrado precisa ser maior que 0!\n")


def erro_sexo():
    print("\ninforme sexo: 'f' ou 'm'!\n")


def erro_estad_civ():
    print("\nEstado Civil: 's' - solteiro.")
    print("              'c' - casado.")
    print("              'v' - viuvo.")
    print("              'd' - divorciado.\n")


nome = input("digite o nome: ")
idade = int(input("digite a idade: "))
salario = float(input("digite o salario: "))
sexo = input("digite o sexo: ").upper()
estad_civ = input("digite o estado civil: ").upper()

while len(nome) < 3:
    erro_nome()
    nome = input("digite o nome: ")
while idade < 0 and idade > 150:
    erro_idade()
    idade = int(input("digite a idade: "))
while salario <= 0:
    erro_salario()
    salario = float(input("digite o salario: "))
while sexo != 'F' and sexo != 'M':
    erro_sexo()
    sexo = input("digite o sexo: ").upper()
while estad_civ != 'S' and estad_civ != 'C' and estad_civ != 'V' and estad_civ != 'D':
    erro_estad_civ()
    estad_civ = input('digite o estado civil: ').upper()

print(f"\nNome: {nome}.")
print(f"Idade: {idade}.")
print(f"Salário: {salario}.")
print(f"Sexo: {sexo}.")
print(f"Estado Civil: {estad_civ}.")
