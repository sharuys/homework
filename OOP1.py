import random

class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def place_random_pieces(self):
        pieces = ['♚', '♛', '♜', '♝', '♞', '♟']
        for piece in pieces:
            self.place_piece(piece)

    def place_piece(self, piece):
        while True:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if self.board[row][col] == ' ':
                self.board[row][col] = piece
                break

    def draw_board(self):
        for row in reversed(range(8)):
            print('  +------------------------+')
            print(f'{row + 1} |', end=' ')
            for col in range(8):
                print(f'{self.board[row][col]} |', end=' ')
            print()
        print('  +------------------------+')
        print('    a  b  c  d  e  f  g  h')

chess_board = ChessBoard()
chess_board.place_random_pieces()
chess_board.draw_board()
