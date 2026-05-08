while True:
    x = int(input("Digite um valor: "))
    if x % 2 == 0:
        print(f"{x} - Par")
    else:
        print(f"{x} - Impar")
    if x == 2:
        break

print(x)