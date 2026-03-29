# função para calcular o máximo divisor comum usando recursão
def mdc(vicente, ricardo):
    if ricardo == 0:
        return vicente
    elif vicente == 0:
        return ricardo
    return mdc(ricardo, vicente % ricardo) 

# Função para imprimir os resultados
def imprimir_resultados(vicente, ricardo):
    tamanho_pilha = mdc(vicente, ricardo) # tamanho da pilha  = MDC entre vicente e ricardo
    print(f"O tamanho da pilha de figurinhas é: {tamanho_pilha}")

# Função para receber as entradas do usuário
def entradas():
    while True:
        casodeteste = int(input("Digite o número de casos de teste: "))
        if casodeteste < 1 or casodeteste > 3000:
            print("Número de casos de teste deve ser entre 1 e 3000. Tente novamente.")
        else:
            break
    for i in range(casodeteste):
        while True:
            ricardo = int(input("Digite o número de figurinhas que Ricardo tem: "))
            if ricardo < 1 or ricardo > 1000:
                print("Número de figurinhas de Ricardo deve ser entre 1 e 1000. Tente novamente.")
            else:
                break
        
        while True:
            vicente = int(input("Digite o número de figurinhas que Vicente tem: "))
            if vicente < 1 or vicente > 1000:
                print("Número de figurinhas de Vicente deve ser entre 1 e 1000. Tente novamente.")
            else:
                break
    
        imprimir_resultados(vicente, ricardo)

entradas()


        
        