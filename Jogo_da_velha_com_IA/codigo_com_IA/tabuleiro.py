class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO]*3 for _ in range(3)]

    def tem_campeao(self):
        # verifica linhas e colunas
        for i in range(3):
            # linha
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] != Tabuleiro.DESCONHECIDO:
                return self.matriz[i][0]
            # coluna
            if self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] != Tabuleiro.DESCONHECIDO:
                return self.matriz[0][i]

        # diagonais
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][0]
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][2]

        # nenhum campeão
        return Tabuleiro.DESCONHECIDO
