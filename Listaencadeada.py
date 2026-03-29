class No:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)

novo = No(1)
novo.mostrar_no()

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    
    def lista_vazia(self):
        return self.primeiro is None
    
    def mostrar_lista(self):
        if self.lista_vazia():
            print("Lista vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            atual.mostrar_no()
            atual = atual.proximo
    
    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        if self.lista_vazia():
            print("Lista vazia")
        else:
            self.primeiro = self.primeiro.proximo
    
    def excluir_fim(self):
        if self.lista_vazia():
            print("Lista vazia")
        elif self.primeiro.proximo is None:
            self.primeiro = None
        else:
            atual = self.primeiro
            while atual.proximo.proximo is not None:
                atual = atual.proximo
            atual.proximo = None

    def pesquisar(self, valor):
        if self.lista_vazia():
            print("Lista vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
    
    def ordenar_lista(self):
        if self.lista_vazia():
            print("Lista vazia")
            return None
        atual = self.primeiro
        while atual is not None:
            proximo = atual.proximo
            while proximo is not None:
                if atual.valor > proximo.valor:
                    atual.valor, proximo.valor = proximo.valor, atual.valor
                proximo = proximo.proximo
            atual = atual.proximo
    
    def excluir_valor(self,valor):
        if self.lista_vazia():
            print("Lista vazia")

        else:
            atual = self.primeiro
            
            while atual is not None and atual.valor != valor:
                anterior = atual
                atual = atual.proximo
            anterior.proximo  = atual.proximo


        

lista = ListaEncadeada()
lista.mostrar_lista()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)
lista.inserir_inicio(40)
lista.inserir_inicio(50)
lista.inserir_inicio(60)
lista.mostrar_lista()
print(lista.pesquisar(20))
lista.excluir_valor(50)
lista.mostrar_lista()