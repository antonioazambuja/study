from python_string import exerc1, exerc2, exerc3, exerc4, exerc5, exerc6
from python_string import exerc7, exerc8, exerc9, exerc10, exerc11
from python_string import exerc12, exerc13, exerc14, exerc15, exerc16
from python_string import exerc17, exerc18


def exercicios(exerc):
    if exerc == 1:
        print(exerc1.desc())
        exerc1.func()
    elif exerc == 2:
        print(exerc2.desc())
        exerc2.func()
    elif exerc == 3:
        print(exerc3.desc())
        exerc3.func()
    elif exerc == 4:
        print(exerc4.desc())
        exerc4.func()
    elif exerc == 5:
        print(exerc5.desc())
        exerc5.func()
    elif exerc == 6:
        print(exerc6.desc())
        exerc6.func()
    elif exerc == 8:
        print(exerc8.desc())
        exerc8.func()
    elif exerc == 9:
        print(exerc9.desc())
        exerc9.func()
    elif exerc == 10:
        print(exerc10.desc())
        exerc10.func()
    elif exerc == 11:
        print(exerc11.desc())
        exerc11.func()
    elif exerc == 12:
        print(exerc12.desc())
        exerc12.func()
    elif exerc == 13:
        print(exerc13.desc())
        exerc13.func()
    elif exerc == 14:
        print(exerc14.desc())
        exerc14.func()
    elif exerc == 15:
        print(exerc15.desc())
        exerc15.func()
    elif exerc == 16:
        print(exerc16.desc())
        exerc16.func()
    elif exerc == 17:
        print(exerc17.desc())
        exerc17.func()
    elif exerc == 18:
        print(exerc18.desc())
        exerc18.func()
    else:
        print('Exercício inválido!')
    print('------------------\nFIM DA EXECUÇÃO!')


if __name__ == "__main__":
    while True:
        escolha = int(input('\n* Escolha um exercício para executar: '))
        exercicios(escolha)
        if escolha == 0:
            break
