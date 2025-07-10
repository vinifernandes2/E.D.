# -*- coding: utf-8 -*-
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
        self.oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

    def getJogada(self) -> tuple[int, int]:
        # Utilitários para linhas, colunas, diagonais
        def linhas_colunas_diagonais():
            lines = []
            # linhas
            for i in range(3):
                lines.append([(i, j) for j in range(3)])
            # colunas
            for j in range(3):
                lines.append([(i, j) for i in range(3)])
            # diagonais
            lines.append([(i, i) for i in range(3)])
            lines.append([(i, 2 - i) for i in range(3)])
            return lines

        def count_marks(line, player):
            return sum(1 for (x,y) in line if self.matriz[x][y] == player)

        def empty_in_line(line):
            return [pos for pos in line if self.matriz[pos[0]][pos[1]] == Tabuleiro.DESCONHECIDO]

        # R1 - Vencer ou bloquear:
        for player in [self.tipo, self.oponente]:
            for line in linhas_colunas_diagonais():
                if count_marks(line, player) == 2:
                    empties = empty_in_line(line)
                    if len(empties) == 1:
                        return empties[0]

        # R2 - Criar um fork (duas sequências de 2)
        def is_fork_move(pos):
            x, y = pos
            if self.matriz[x][y] != Tabuleiro.DESCONHECIDO:
                return False
            count = 0
            for line in linhas_colunas_diagonais():
                if pos in line:
                    # conta linhas onde já tenho 1 marcação e pelo menos 2 vazios (sugere possibilidade de 2 em sequência)
                    if count_marks(line, self.tipo) == 1 and len(empty_in_line(line)) == 2:
                        count += 1
            return count >= 2

        forks = []
        for i in range(3):
            for j in range(3):
                if is_fork_move((i,j)):
                    forks.append((i,j))
        if forks:
            return forks[0]

        # R3 - Centro livre
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1,1)

        # R4 - Oponente marcou um canto, marque o canto oposto
        cantos = [(0,0), (0,2), (2,0), (2,2)]
        for c in cantos:
            ox, oy = 2 - c[0], 2 - c[1]  # canto oposto
            if self.matriz[c[0]][c[1]] == self.oponente and self.matriz[ox][oy] == Tabuleiro.DESCONHECIDO:
                return (ox, oy)

        # R5 - Marcar qualquer canto vazio
        for c in cantos:
            if self.matriz[c[0]][c[1]] == Tabuleiro.DESCONHECIDO:
                return c

        # R6 - Marcar arbitrariamente qualquer quadrado vazio
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                    return (i, j)

        return None  # sem jogadas possíveis (empate)
