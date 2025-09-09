class Peca:
    def __init__(self, nome, cor):
        self.nome = nome  # P, T, C, B, Q, K
        self.cor = cor  # 'w' ou 'b'

    def __str__(self):
        return f"{self.cor}{self.nome}"

class Xadrez:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.turno = 'w'  # 'w' começa

    def criar_tabuleiro(self):
        T, C, B, Q, K, P = 'T', 'C', 'B', 'Q', 'K', 'P'
        vazio = None
        brancas = [Peca(T, 'w'), Peca(C, 'w'), Peca(B, 'w'), Peca(Q, 'w'),
                   Peca(K, 'w'), Peca(B, 'w'), Peca(C, 'w'), Peca(T, 'w')]
        pretas  = [Peca(T, 'b'), Peca(C, 'b'), Peca(B, 'b'), Peca(Q, 'b'),
                   Peca(K, 'b'), Peca(B, 'b'), Peca(C, 'b'), Peca(T, 'b')]
        tab = [
            pretas,
            [Peca(P, 'b') for _ in range(8)],
            [vazio] * 8,
            [vazio] * 8,
            [vazio] * 8,
            [vazio] * 8,
            [Peca(P, 'w') for _ in range(8)],
            brancas
        ]
        return tab

    def mostrar_tabuleiro(self):
        print("  a  b  c  d  e  f  g  h")
        for i, linha in enumerate(self.tabuleiro):
            print(8 - i, end=' ')
            for peca in linha:
                print(str(peca) if peca else ' . ', end=' ')
            print(8 - i)
        print("  a  b  c  d  e  f  g  h")

    def posicao_valida(self, pos):
        if len(pos) != 2:
            return False
        colunas = 'abcdefgh'
        linhas = '12345678'
        return pos[0] in colunas and pos[1] in linhas

    def pos_para_idx(self, pos):
        colunas = 'abcdefgh'
        col = colunas.index(pos[0])
        lin = 8 - int(pos[1])
        return lin, col

    def mover(self, de, para):
        if not self.posicao_valida(de) or not self.posicao_valida(para):
            print("Posição inválida! Use coordenadas como e2 e4.")
            return False
        lin1, col1 = self.pos_para_idx(de)
        lin2, col2 = self.pos_para_idx(para)

        peca = self.tabuleiro[lin1][col1]
        destino = self.tabuleiro[lin2][col2]

        if not peca:
            print("Não há peça na posição de origem.")
            return False
        if peca.cor != self.turno:
            print("Não é o turno dessa cor.")
            return False
        if destino and destino.cor == peca.cor:
            print("Você não pode capturar sua própria peça.")
            return False
        # Aqui pode ser feita a validação real do movimento da peça

        self.tabuleiro[lin2][col2] = peca
        self.tabuleiro[lin1][col1] = None
        self.turno = 'b' if self.turno == 'w' else 'w'
        return True

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            print(f"Turno: {'Brancas' if self.turno == 'w' else 'Pretas'}")
            jogada = input("Digite sua jogada (ex: e2 e4): ").strip()
            if jogada.lower() in ['sair', 'exit', 'q']:
                break
            try:
                de, para = jogada.split()
                if not self.mover(de, para):
                    print("Jogada inválida.")
            except:
                print("Formato inválido. Use: e2 e4")

if __name__ == "__main__":
    jogo = Xadrez()
    jogo.jogar()