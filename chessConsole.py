import collections
import chess
from colored import fg, bg, attr
import os
from ai import Ai
import chess.pgn
board = chess.Board()


def board_to_game(board):
    game = chess.pgn.Game()

    # Undo all moves.
    switchyard = collections.deque()
    while board.move_stack:
        switchyard.append(board.pop())

    game.setup(board)
    node = game

    # Replay all moves.
    while switchyard:
        move = switchyard.pop()
        node = node.add_variation(move)
        board.push(move)

    game.headers["Result"] = board.result()
    return game


def boardToMatrix(board):
    pgn = board.epd()
    foo = []
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('x')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo


def makeBoard(matrixBoard):
    print("     a b c d e f g h     ")

    print()
    cnt = 0
    for i in range(len(matrixBoard)):
        print(len(matrixBoard) - i, "  ", end=" ")
        for j in range(len(matrixBoard[i])):
            piece = matrixBoard[i][j]
            if piece == piece.lower():
                color = fg("#d73926")
            else:
                color = fg('#4a8793')
            reset = attr('reset')
            if(piece.lower() == "p"):
                print(color + "p" + reset, end=" ")
            elif(piece.lower() == "r"):
                print(color + "R" + reset, end=" ")
            elif(piece.lower() == "b"):
                print(color + "B" + reset, end=" ")
            elif(piece.lower() == "n"):
                print(color + "N" + reset, end=" ")
            elif(piece.lower() == "q"):
                print(color + "Q" + reset, end=" ")
            elif(piece.lower() == "k"):
                print(color + "K" + reset, end=" ")
            else:
                print("x" + reset, end=" ")
        print("  ", len(matrixBoard) - i, "  ")
    print()
    print("     a b c d e f g h     ")


times = 0

matrixBoard = boardToMatrix(board)
makeBoard(matrixBoard)
while not(board.is_checkmate()):
    if times % 2 == 0:
        move = input('White Plays : ')
    else:
        ai = Ai(board)
        print("Ai is Thinking ...")
        move = ai.ChooseBestMove(1)
    times += 1

    isNotValidMove = True
    while (isNotValidMove):
        try:
            if times % 2:
                board.push_san(move)
            else:
                board.push(move)
            isNotValidMove = False
        except:
            print("The Move isn't Valid")
            move = input('White Plays : ')

    os.system('cls')
    matrixBoard = boardToMatrix(board)
    makeBoard(matrixBoard)
print(board_to_game(board))
