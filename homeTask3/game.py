class TicTacToe:
   

    def __init__(self) -> None:

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def draw_board(self) -> None:
    
        print('-------------')
        for row in self.board:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print('\n-------------')

    def make_move(self, row: int, col: int) -> bool:

        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self, player: str) -> bool:

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def play(self) -> None:

        while True:
            self.draw_board()
            print('Ход игрока', self.current_player)
            rowi = int(input('Выбери строку (1-3): '))
            coli = int(input('Выбери столбец (1-3): '))

            row=rowi-1
            col=coli-1

            if row < 0 or row > 2 or col < 0 or col > 2:
                print('Такой клетки нет! Выбери другую.')
                continue

            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.draw_board()
                    print('Игрок', self.current_player, 'победил!')
                    break

                if all(cell != ' ' for row in self.board for cell in row):
                    self.draw_board()
                    print('Победила дружба!')
                    break

            else:
                print('Клетка занята. Выбери другую.')