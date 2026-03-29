def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    N = int(input("digite o número de termos da sequência de Fibonacci entre 0 e 46: "))

    if 0 <= N <= 46:
        break
    else:
        print("Número inválido. Por favor, digite um número entre 0 e 46.")

for i in range(N):
    if i > 0:
        print(" ", end="")
    print(fibonacci(i), end="")
print()