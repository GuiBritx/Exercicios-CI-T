nome = "Guilherme Brito Pinheiro"
ra  = "N8680D9"
turma = "CC2P12"

print("Nome: ", nome)
print("RA: ", ra)
print("Turma: ", turma)


# exercicio 1
# num = (input("Digite um número, de um a dez: "))

# if num in ['1', '2', '3']:
#     print("O númmero elevado ao quadrado é: ", (int(num)**2))
# elif num in ['4', '9']:
#     print("A raiz quadrada do número é: ", (int(num)**(1/2)))
# elif num in ['6', '7', '8']:
#     print("O número dividido por 9 é: ", (int(num) / 9))
# else:
#     print("Número inválido!")

#exercicio 2
# nome = input("Digite o nome: ")
# ra = input("Digite o RA: ")
# nota1 = input("Digite a primeira nota: ")
# nota2 = input("Digite a segunda nota: ")
# media = (float(nota1) + float(nota2)) / 2

# if media >=7:
#     print("Parabéns, você está aprovado!")
# elif media < 7:
#     print("Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.")

#exercicio 3
# nome = input("Digite o nome: ")
# ra = input("Digite o RA: ")
# nota1 = input("Digite a primeira nota: ")
# nota2 = input("Digite a segunda nota: ")
# media = (float(nota1) + float(nota2)) / 2
# exame = input("Digite a nota do exame: ")
# mediafinal = (media + float(exame)) / 2

# if mediafinal >= 5:
#     print("Parabéns, você aproveitou a sua chance! Está aprovado.")
# elif mediafinal < 5:
#     print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")

#exercicio 4
# def ft(x): return 1 if x == 0 else x * ft(x - 1)
# read_value = int(input("Digite um valor: "))

# if read_value == 1 or read_value == 2:
#     print(read_value ** 3)
# elif read_value % 3 == 0:
#     print(ft(read_value))
# elif read_value == 4 or read_value == 5 or read_value == 7 or read_value == 8:
#     print(read_value / 9)
# else:
#     print("Valor inválido!")

#exercicio 5
# value = float(input("Digite o valor da compra: "))
# if value > 300:
#     discount = 20
# elif value >= 200 and value <= 299.99:
#     discount = 10
# else:
#     discount = 5

# print(f"Valor total: R$ {value}")
# print(f"Valor final: R$ {value - (value * discount / 100)}")

#exercicio 6
# read_value = int(input("Digite um valor: "))
# if read_value < 0:
#     print(abs(read_value))
# elif read_value > 10:
#     read_value2 = int(input("Digite outro valor: "))
#     print(read_value - read_value2)
# else:
#     print(read_value / 5)

#exercicio 7
# read_value = int(input("Digite um valor: "))
# if read_value % 10 == 0:
#     print( "Divisível por 10")
# elif read_value % 5 == 0:
#     print( "Divisível por 5")
# elif read_value % 2 == 0:
#     print( "Divisível por 2")
# else:
#     print("Não é divisível por nenhum desses valores")

#exercicio 8
# salary = float(input("Digite o salário: "))
# if salary <= 1500:
#     increase = 20
# elif salary > 1500 and salary < 2500:
#     increase = 10
# else:
#     increase = 5

# print( f"Salário final: R$ {salary + (salary * increase / 100)}")

#exercicio 9
# name = input("Digite seu nome: ")
# age = int(input("Digite sua idade: "))

# if age >= 18:
#     if age >= 65:
#         print(f"Bem vindo {name} você é maior de 65 anos.")
#     else:
#         print(f"Bem vindo {name} você é maior de idade.")
# else:
#     print(f"Bem vindo {name} você é menor de idade.")

# Parte II - Questionário

# 1. C
# 2. A
# 3. C
# 4. B
# 5. C
# 6. C