class No:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        self.proximo = None

class lista:
    def __init__(self):
        self.primeiro = None
    
    def inserir_produto(self, codigo, nome, preco, quantidade):
        novo = No(codigo, nome, preco, quantidade)
        if self.primeiro is None:
            self.primeiro = novo
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

    def relatorio(self):
        atual = self.primeiro
        while atual is not None:
            print(f"Código: {atual.codigo} Produto: {atual.nome} Quantidade: {atual.quantidade} R$: {atual.preco}")

            atual = atual.proximo 

    def atualizar_quantidades(self, codigo, quantidade):
        
        procura = self.primeiro
        if procura is None:
            print("Lista Vazia!")
            return
        
        while procura.codigo != codigo:
            if procura.proximo is None:
                print("Produto não encontrado")
                return  
           
                
            else:
                procura = procura.proximo

        
        procura.quantidade = quantidade

def main():
    estoque = lista()
    while True:
        print("\n------- SISTEMA DE ESTOQUE -------")
        print("1 - Cadastro de produto")
        print("2 - Exibir relatório")
        print("3 - Excluir produto")
        print("4 - Atualizar Quantidades")
        resposta = input()


        if resposta == "1":
            estoque.inserir_produto()
    


if __name__ == "__main__":
    main()
