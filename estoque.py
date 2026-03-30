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

    def buscar(self, codigo):
        atual = self.primeiro
        while atual is not None:
            if atual.codigo == codigo:
                return atual
            atual = atual.proximo
        return None

    def excluir(self, codigo):
        atual = self.primeiro
        anterior = None

        while atual is not None:
            if atual.codigo == codigo:
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                print("Produto removido!")
                return
            anterior = atual
            atual = atual.proximo

        print("Produto não encontrado!")

def main():
    estoque = lista()
    while True:
        print("\n------- SISTEMA DE ESTOQUE -------")
        print("1 - Cadastro de produto")
        print("2 - Exibir relatório")
        print("3 - Excluir produto")
        print("4 - Atualizar Quantidades")
        print("5 - Buscar produto")
        print("0 - Sair do sistema")
        
        resposta = input("Escolha uma opção: ")

        if resposta == "1":
            codigo = input("Código: ")
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            estoque.inserir_produto(codigo, nome, preco, quantidade)
            print("Produto cadastrado com sucesso!")
            
        elif resposta == "2":
            print("\n--- Relatório de Estoque ---")
            estoque.relatorio()
            
        elif resposta == "3":
            codigo = input("Digite o código do produto a ser excluído: ")
            estoque.excluir(codigo)
            
        elif resposta == "4":
            codigo = input("Digite o código do produto: ")
            
            produto_encontrado = estoque.buscar(codigo)
            
            if produto_encontrado is not None:
                print(f"Produto atual: {produto_encontrado.nome} | Estoque: {produto_encontrado.quantidade}")
                quantidade = int(input("Digite a nova quantidade: "))
                
                estoque.atualizar_quantidades(codigo, quantidade)
                print("Quantidade atualizada com sucesso!")
            else:
                print("Produto não encontrado no estoque! Não é possível atualizar.")
            
        elif resposta == "5":
            codigo = input("Digite o código do produto que deseja buscar: ")
         
            produto_encontrado = estoque.buscar(codigo)

            if produto_encontrado is not None:
                print(f"\nProduto encontrado: {produto_encontrado.nome}")
                print(f"Preço: R$ {produto_encontrado.preco} | Quantidade em estoque: {produto_encontrado.quantidade}")
            else:
                print("Produto não encontrado no estoque!")
                
        elif resposta == "0":
            print("Saindo do sistema. Até logo!")
            break 
            
        else:
            print("Opção inválida! Por favor, escolha um número de 0 a 5.")

if __name__ == "__main__":
    main()
