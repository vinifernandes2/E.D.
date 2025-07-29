class ListaSeq:
    def __init__(self, capacidade=100):
        self.tam_max = capacidade
        self.dados = [0] * self.tam_max
        self.tam_atual = 0

    def vazia(self):
        return self.tam_atual == 0

    def cheia(self):
        return self.tam_atual == self.tam_max

    def tamanho(self):
        return self.tam_atual

    def elemento(self, pos):
        if pos <= 0 or pos > self.tam_atual:
            return -1
        return self.dados[pos - 1]

    def modificar(self, pos, novo_valor):
        if pos <= 0 or pos > self.tam_atual:
            return False
        self.dados[pos - 1] = novo_valor
        return True

    def posicao(self, valor):
        for i in range(self.tam_atual):
            if self.dados[i] == valor:
                return i + 1
        return -1

    def insere(self, pos, valor):
        if self.cheia() or pos <= 0 or pos > self.tam_atual + 1:
            return False
        for i in range(self.tam_atual, pos - 1, -1):
            self.dados[i] = self.dados[i - 1]
        self.dados[pos - 1] = valor
        self.tam_atual += 1
        return True

    def remove(self, pos):
        if pos < 1 or pos > self.tam_atual:
            return -1
        valor = self.dados[pos - 1]
        for i in range(pos - 1, self.tam_atual - 1):
            self.dados[i] = self.dados[i + 1]
        self.tam_atual -= 1
        return valor
