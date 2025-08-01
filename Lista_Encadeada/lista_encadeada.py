class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.cabeca is None

    def obter_tamanho(self):
        return self.tamanho

    def obter_valor(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        return atual.valor

    def modificar_valor(self, posicao, novo_valor):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        atual.valor = novo_valor

    def inserir(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho + 1:
            raise IndexError("Posição inválida.")
        novo_no = No(valor)
        if posicao == 1:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            anterior = self.cabeca
            for _ in range(posicao - 2):
                anterior = anterior.proximo
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no
        self.tamanho += 1

    def retirar(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        if posicao == 1:
            removido = self.cabeca
            self.cabeca = self.cabeca.proximo
        else:
            anterior = self.cabeca
            for _ in range(posicao - 2):
                anterior = anterior.proximo
            removido = anterior.proximo
            anterior.proximo = removido.proximo
        self.tamanho -= 1
        return removido.valor

    def imprimir(self):
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(" -> ".join(elementos) if elementos else "Lista vazia.")
