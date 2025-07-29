from lista_sequencial import ListaSeq

def menu():
    print("\n--- MENU ---")
    print("1. Inserir elemento")
    print("2. Remover elemento")
    print("3. Verificar se a lista está vazia")
    print("4. Verificar se a lista está cheia")
    print("5. Tamanho da lista")
    print("6. Acessar elemento por posição")
    print("7. Modificar elemento por posição")
    print("8. Buscar posição de um valor")
    print("9. Mostrar todos os elementos")
    print("0. Sair")

def main():
    lista = ListaSeq()

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido")
            continue

        if opcao == 1:
            pos = int(input("Posição para inserir (1 até tamanho+1): "))
            valor = int(input("Valor a ser inserido: "))
            if lista.insere(pos, valor):
                print("Inserido com sucesso.")
            else:
                print("Falha ao inserir (posição inválida ou lista cheia).")

        elif opcao == 2:
            pos = int(input("Posição para remover: "))
            removido = lista.remove(pos)
            if removido == -1:
                print("Falha na remoção (posição inválida).")
            else:
                print(f"Elemento removido: {removido}")

        elif opcao == 3:
            print("Lista vazia?" , "Sim" if lista.vazia() else "Não")

        elif opcao == 4:
            print("Lista cheia?" , "Sim" if lista.cheia() else "Não")

        elif opcao == 5:
            print("Tamanho da lista:", lista.tamanho())

        elif opcao == 6:
            pos = int(input("Posição do elemento que deseja ver: "))
            valor = lista.elemento(pos)
            if valor == -1:
                print("Posição inválida.")
            else:
                print("Valor encontrado:", valor)

        elif opcao == 7:
            pos = int(input("Posição do elemento a modificar: "))
            novo = int(input("Novo valor: "))
            if lista.modificar(pos, novo):
                print("Modificado com sucesso.")
            else:
                print("Falha ao modificar (posição inválida).")

        elif opcao == 8:
            valor = int(input("Valor a buscar: "))
            pos = lista.posicao(valor)
            if pos == -1:
                print("Valor não encontrado.")
            else:
                print(f"Valor está na posição {pos}.")

        elif opcao == 9:
            print("Elementos na lista:")
            for i in range(1, lista.tamanho() + 1):
                print(f"{i}: {lista.elemento(i)}")

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
