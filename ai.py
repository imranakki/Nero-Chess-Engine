import chess
import chess.polyglot


class Ai:

    def __init__(self, board) -> None:
        self.board = board
        # the most favorable position of each piece
        self.PawnTable = [
            0, 0, 0, 0, 0, 0, 0, 0,
            5, 10, 10, -20, -20, 10, 10, 5,
            5, -5, -10, 0, 0, -10, -5, 5,
            0, 0, 0, 20, 20, 0, 0, 0,
            5, 5, 10, 25, 25, 10, 5, 5,
            10, 10, 20, 30, 30, 20, 10, 10,
            50, 50, 50, 50, 50, 50, 50, 50,
            0, 0, 0, 0, 0, 0, 0, 0]

        self.KnightsTable = [
            -50, -40, -30, -30, -30, -30, -40, -50,
            -40, -20, 0, 5, 5, 0, -20, -40,
            -30, 5, 10, 15, 15, 10, 5, -30,
            -30, 0, 15, 20, 20, 15, 0, -30,
            -30, 5, 15, 20, 20, 15, 5, -30,
            -30, 0, 10, 15, 15, 10, 0, -30,
            -40, -20, 0, 0, 0, 0, -20, -40,
            -50, -40, -30, -30, -30, -30, -40, -50]

        self.BishopsTable = [
            -20, -10, -10, -10, -10, -10, -10, -20,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -10, 10, 10, 10, 10, 10, 10, -10,
            -10, 0, 10, 10, 10, 10, 0, -10,
            -10, 5, 5, 10, 10, 5, 5, -10,
            -10, 0, 5, 10, 10, 5, 0, -10,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -20, -10, -10, -10, -10, -10, -10, -20]

        self.RooksTable = [
            0, 0, 0, 5, 5, 0, 0, 0,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            5, 10, 10, 10, 10, 10, 10, 5,
            0, 0, 0, 0, 0, 0, 0, 0]

        self.QueensTable = [
            -20, -10, -10, -5, -5, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 5, 5, 5, 5, 5, 0, -10,
            0, 0, 5, 5, 5, 5, 0, -5,
            -5, 0, 5, 5, 5, 5, 0, -5,
            -10, 0, 5, 5, 5, 5, 0, -10,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -20, -10, -10, -5, -5, -10, -10, -20]

        self.KingTable = [
            20, 30, 10, 0, 0, 10, 30, 20,
            20, 20, 0, 0, 0, 0, 20, 20,
            -10, -20, -20, -20, -20, -20, -20, -10,
            -20, -30, -30, -40, -40, -30, -30, -20,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30]

    def evaluate_board(self):
        board = self.board
        PawnTable, KnightsTable, BishopsTable, RooksTable, QueensTable, KingTable = self.PawnTable, self.PawnTable, self.BishopsTable, self.RooksTable, self.QueensTable, self.KingTable

        if board.is_checkmate():
            if board.turn:
                return -9999
            else:
                return 9999

        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0

        WhitePawn = len(board.pieces(chess.PAWN, chess.WHITE))
        BlackPawn = len(board.pieces(chess.PAWN, chess.BLACK))
        WhiteKnight = len(board.pieces(chess.KNIGHT, chess.WHITE))
        BlackKnight = len(board.pieces(chess.KNIGHT, chess.BLACK))
        WhiteBishop = len(board.pieces(chess.BISHOP, chess.WHITE))
        BlackBishop = len(board.pieces(chess.BISHOP, chess.BLACK))
        WhiteRook = len(board.pieces(chess.ROOK, chess.WHITE))
        BlackRook = len(board.pieces(chess.ROOK, chess.BLACK))
        WhiteQueen = len(board.pieces(chess.QUEEN, chess.WHITE))
        BlackQueen = len(board.pieces(chess.QUEEN, chess.BLACK))

        # material score
        Material = 100 * (WhitePawn - BlackPawn) + 320 * (WhiteKnight - BlackKnight) \
            + 330 * (WhiteBishop - BlackBishop) + 500 * (WhiteRook - BlackRook) \
            + 900 * (WhiteQueen - BlackQueen)

        PawnSQ = sum([PawnTable[i]
                      for i in board.pieces(chess.PAWN, chess.WHITE)]) \
            + sum([-PawnTable[chess.square_mirror(i)]
                   for i in board.pieces(chess.PAWN, chess.BLACK)])

        KnightSQ = sum([KnightsTable[i]
                        for i in board.pieces(chess.KNIGHT, chess.WHITE)]) \
            + sum([-KnightsTable[chess.square_mirror(i)]
                   for i in board.pieces(chess.KNIGHT, chess.BLACK)])

        BishopSQ = sum([BishopsTable[i]
                        for i in board.pieces(chess.BISHOP, chess.WHITE)]) \
            + sum([-BishopsTable[chess.square_mirror(i)]
                   for i in board.pieces(chess.BISHOP, chess.BLACK)])

        RookSQ = sum([RooksTable[i]
                      for i in board.pieces(chess.ROOK, chess.WHITE)]) \
            + sum([-RooksTable[chess.square_mirror(i)]
                   for i in board.pieces(chess.ROOK, chess.BLACK)])

        QueenSQ = sum([QueensTable[i]
                       for i in board.pieces(chess.QUEEN, chess.WHITE)]) \
            + sum([-QueensTable[chess.square_mirror(i)]
                   for i in board.pieces(chess.QUEEN, chess.BLACK)])
        KingSQ = sum([KingTable[i]
                      for i in board.pieces(chess.KING, chess.WHITE)]) \
            + sum([-KingTable[chess.square_mirror(i)]
                   for i in board.pieces(chess.KING, chess.BLACK)])
        eval = Material + PawnSQ + KnightSQ + BishopSQ + RookSQ + QueenSQ + KingSQ
        if board.turn:
            return eval
        else:
            return -eval

    def ChooseBestMove(self, depth):
        board = self.board
        try:
            move = chess.polyglot.MemoryMappedReader(
                "./human.bin").weighted_choice(board).move
            return move
        except:
            bestMove = chess.Move.null()
            bestValue = -99999
            alpha = -100000
            beta = 100000
            for move in board.legal_moves:
                board.push(move)
                boardValue = -self.alphabeta(-beta, -alpha, depth - 1)
                if boardValue > bestValue:
                    bestValue = boardValue
                    bestMove = move
                if (boardValue > alpha):
                    alpha = boardValue
                board.pop()
            return bestMove

    def alphabeta(self, alpha, beta, depthleft):
        board = self.board
        bestscore = -9999
        if (depthleft == 0):
            return self.quiesce(alpha, beta)
        for move in board.legal_moves:
            board.push(move)
            score = -self.alphabeta(-beta, -alpha, depthleft - 1)
            board.pop()
            if (score >= beta):
                return score
            if (score > bestscore):
                bestscore = score
            if (score > alpha):
                alpha = score
        return bestscore

    def quiesce(self, alpha, beta):
        stand_pat = self.evaluate_board()
        board = self.board
        if (stand_pat >= beta):
            return beta
        if (alpha < stand_pat):
            alpha = stand_pat

        for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                score = -self.quiesce(-beta, -alpha)
                board.pop()

                if (score >= beta):
                    return beta
                if (score > alpha):
                    alpha = score
        return alpha
