import enum


class Mark(enum.IntEnum):
    _ = 0
    x = 1
    o = 2

    def __repr__(self) -> str:
        return self._name_


class Game:
    def __init__(self, filled_tiles):
        self.board = [Mark._ for _ in range(9)]
        self.filled_tiles = filled_tiles

    def __repr__(self) -> str:
        b = self.board
        return f"""Board
        {" ".join(map(repr, b[0:3]))}
        {" ".join(map(repr, b[3:6]))}
        {" ".join(map(repr, b[6:9]))}
        """

    def is_winner(self, player):
        b = self.board
        if b[0] == b[1] == b[2] == player:
            return True
        if b[3] == b[4] == b[5] == player:
            return True
        if b[6] == b[7] == b[8] == player:
            return True
        if b[0] == b[3] == b[6] == player:
            return True
        if b[1] == b[4] == b[7] == player:
            return True
        if b[2] == b[5] == b[8] == player:
            return True
        if b[0] == b[4] == b[8] == player:
            return True
        if b[6] == b[4] == b[2] == player:
            return True
        else:
            return False

    def is_draw(self):
        no_of_marked_tiles = self.marked_tiles()
        if no_of_marked_tiles == 9:
            return True
        else:
            return False

    def marked_tiles(self):
        return sum(Mark._ != _ for _ in self.board)

    def update_board(self, tile: int):
        b = self.board
        if b[tile] == Mark._:
            no_of_marked_tiles = self.marked_tiles()
            n_even_marked_tiles = no_of_marked_tiles % 2 == 0
            b[tile] = repr(Mark.x) if n_even_marked_tiles else repr(Mark.o)
            self.filled_tiles.append(tile)
            print(self)
        else:
            print("tile already picked")

    def undo(self):
        if self.marked_tiles() != 0:
            self.board[self.filled_tiles[-1]] = Mark._
            self.filled_tiles.pop()
            print(self)
        else:
            print("cant undo")


class main:
    filled_tiles = []
    game = Game(filled_tiles)
    print(game)
    while True:
        input1 = int(input("pick a tile "))
        if input1 == -1:
            game.undo()
        else:
            game.update_board(input1)

        x_winner = game.is_winner("x")
        o_winner = game.is_winner("o")
        is_draw = game.is_draw()
        if x_winner:
            print("x is the winner")
            break
        if o_winner:
            print("o is the winner")
            break
        if is_draw:
            print("its a draw")
            break
