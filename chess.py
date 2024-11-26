from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'{self.__class__.__name__}({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        if self.color == "white":
            forward = (row + 1, col)
            if self.is_position_on_board(forward):
                moves.append(forward)
            if row == 2:  
                double_forward = (row + 2, col)
                if self.is_position_on_board(double_forward):
                    moves.append(double_forward)

        elif self.color == "black":
            forward = (row - 1, col)
            if self.is_position_on_board(forward):
                moves.append(forward)
            if row == 7:  
                double_forward = (row - 2, col)
                if self.is_position_on_board(double_forward):
                    moves.append(double_forward)

        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for d in range(1, 8):
            directions = [
                (row + d, col + d), (row + d, col - d),
                (row - d, col + d), (row - d, col - d)
            ]
            for move in directions:
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for d in range(1, 8):
            directions = [
                (row + d, col), (row - d, col),
                (row, col + d), (row, col - d)
            ]
            for move in directions:
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        
        for d in range(1, 8):
            directions = [
                (row + d, col + d), (row + d, col - d),
                (row - d, col + d), (row - d, col - d)
            ]
            for move in directions:
                if self.is_position_on_board(move):
                    moves.append(move)


        for d in range(1, 8):
            directions = [
                (row + d, col), (row - d, col),
                (row, col + d), (row, col - d)
            ]
            for move in directions:
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())

    


