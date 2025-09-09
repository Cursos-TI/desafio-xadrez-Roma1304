import chess
import chess.engine

# Caminho para o motor Stockfish
STOCKFISH_PATH = "/caminho/para/stockfish"  # Altere para o caminho correto!

board = chess.Board()

with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
    while not board.is_game_over():
        print(board.unicode())
        if board.turn == chess.WHITE:
            move = input("Seu lance (ex: e2e4): ")
            try:
                board.push_uci(move)
            except ValueError:
                print("Lance inválido! Tente novamente.")
                continue
        else:
            result = engine.play(board, chess.engine.Limit(time=1))
            print(f"Stockfish joga: {result.move}")
            board.push(result.move)
    print("Fim de jogo:", board.result())