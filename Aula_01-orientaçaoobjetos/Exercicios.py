"""Exercicio 1 Leia a idade de uma pessoa e informe se ela é maior ou menor de idade."""   # control ; para deixar varios como leitura #
idade = int(input("Qual sua idade: "))

if idade >= 18:
    print(f"Você é maior de idade")
else:
    print("Você é menor de idade")

    """Exercicio 2: Leia um número e informe se ele é positivo ou negativo"""
numero = int(input("Coloque um número "))
if numero >= 0:
    print(f"O {numero} é positivo")
else:
    print(f"o numero é negativo")    

    """Exercicio numero 3 Leia um numero e informe se ele é par ou impar"""

numero_3 = int(input("Coloque um numero")) 

if numero_3 % 2 == 0: 
    print(f"O {numero_3} é par: ")
else:
    print(f"O numero {numero} é impar")

"""Exercicio 4 Leia dois numeros e informe qual é o maior"""

numero_1 = int(input("Coloque um numero "))
numero_2 = int(input("Coloque outro numero "))

if numero_1 > numero_2:
    print(f"o numero {numero_1} é maior")
else:
    print(f"o numero {numero_2} é menor ")    

    """ Exercicio 5: Leia a nota de um aluno e informe se ele foi aprovado (nota maior ou igual a 6) ou reprovado."""

nota_aluno = float(input("Digite sua nota: "))

if nota_aluno >= 6:
    print(f"Aluno aprovado, sua nota foi {nota_aluno}")    
else:
    print(f"Aluno Reprovado, sua nota foi {nota_aluno}")

    """ Exercicio 6: Leia o salario de um funcionario e informe se ele recebe acima ou abaixo de R$ 3000.00"""

salario = float(input("Quanto você recebe? " ))

if salario >= 3000.00:
        print(f"Você Recebe acima/igual 3000.00")
else: 
    print(f"Você recebe menos de 3000.00")

"""Exercicio 7: Leia um número e informe se ele é multiplo de 5"""
numero_4 = int(input("Coloque um numero inteiro"))

if numero_4 % 5 == 0:
    print(f"O número {numero_4} é Multiplo de 5")
else:
    print(f"O número {numero_4} Não é Multiplo de 5")    