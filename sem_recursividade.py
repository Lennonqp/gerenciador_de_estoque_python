def sem_recursividade(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado