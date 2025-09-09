def criar_tabuleiro():
    return [
        ['♜','♞','♝','♛','♚','♝','♞','♜'],
        ['♟','♟','♟','♟','♟','♟','♟','♟'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['♙','♙','♙','♙','♙','♙','♙','♙'],
        ['♖','♘','♗','♕','♔','♗','♘','♖'],
    ]

def mostrar_tabuleiro(tabuleiro):
    print("  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):
            print(tabuleiro[i][j], end=" ")
        print(8 - i)
    print("  a b c d e f g h\n")

def coordenada_valida(pos):
    if len(pos) != 2:
        return False
    colunas = 'abcdefgh'
    linhas = '12345678'
    return pos[0] in colunas and pos[1] in linhas

def converter_posicao(pos):
    colunas = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    linha = 8 - int(pos[1])
    coluna = colunas[pos[0]]
    return linha, coluna

def cor_peca(peca):
    if peca in '♜♞♝♛♚♟':
        return 'preta'
    elif peca in '♖♘♗♕♔♙':
        return 'branca'
    return None

def mover_peca(tabuleiro, origem, destino, turno_branco):
    if not coordenada_valida(origem) or not coordenada_valida(destino):
        print("Coordenada inválida! Use o formato indicado, ex: e2.")
        return False

    linha_origem, col_origem = converter_posicao(origem)
    linha_destino, col_destino = converter_posicao(destino)
    peca = tabuleiro[linha_origem][col_origem]
    destino_peca = tabuleiro[linha_destino][col_destino]

    if peca == '.':
        print("Não há peça nessa posição!")
        return False

    cor = cor_peca(peca)
    if (turno_branco and cor != 'branca') or (not turno_branco and cor != 'preta'):
        print("Essa peça não é sua!")
        return False

    if destino_peca != '.' and cor_peca(destino_peca) == cor:
        print("Não pode capturar sua própria peça!")
        return False

    tabuleiro[linha_destino][col_destino] = peca
    tabuleiro[linha_origem][col_origem] = '.'
    return True

def jogar():
    tabuleiro = criar_tabuleiro()
    turno_branco = True

    while True:
        mostrar_tabuleiro(tabuleiro)
        jogador = "Brancas" if turno_branco else "Pretas"
        print(f"Turno das {jogador}")

        origem = input("Mover de (ex: e2): ").strip().lower()
        destino = input("Mover para (ex: e4): ").strip().lower()

        if origem == 'sair' or destino == 'sair':
            print("Jogo encerrado.")
            break

        if mover_peca(tabuleiro, origem, destino, turno_branco):
            turno_branco = not turno_branco
        else:
            print("Movimento inválido. Tente novamente.")

jogar()