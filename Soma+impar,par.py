A = (int(input("Digite um valor para A: ")))
B = (int(input("Digite um valor para B: ")))
Soma = A + B
print("Soma: ", Soma)
Divisao = A / B
print("Divisao: ", Divisao)
Subtracao = A - B
print("Subtracao: ", Subtracao)
Multiplicacao = A * B
print("Multiplicacao: ", Multiplicacao)
Resolucao = Divisao + Multiplicacao
print("Resolucao: ", Resolucao)

if Soma % 2 == 0:
    print("Soma é par")
else:
    print("Soma é impar")

if Subtracao % 2 == 0:
    print("Subtracao é par")
else:
    print("Subtracao é impar")

if Multiplicacao % 2 == 0:
    print("Multiplicacao é par")
else:
    print("Multiplicacao é impar")

if Resolucao % 2 == 0:
    print("Resolucao é par")
else:
    print("Resolucao é impar")