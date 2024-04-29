import enum
import pickle
import os
import abc
from dataclasses import dataclass, field


class Mark(enum.IntEnum):
    _ = 0
    x = 1
    o = 2

    def __repr__(self) -> str:
        return self._name_

    def __str__(self) -> str:
        return self._name_


@dataclass
class Game:
    board: list = field(default_factory=lambda: [Mark._ for _ in range(9)])
    filled_tiles: list = field(default_factory=list)

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

    def apply(self, action: "Action"):
        return action.execute(self)


class Action(abc.ABC):
    @abc.abstractmethod
    def execute(self, game: Game): ...


@dataclass
class Update(Action):
    tile: int

    def execute(self, game: Game):
        b = game.board
        if b[self.tile] == Mark._:
            no_of_marked_tiles = game.marked_tiles()
            n_even_marked_tiles = no_of_marked_tiles % 2 == 0
            b[self.tile] = repr(Mark.x) if n_even_marked_tiles else repr(Mark.o)
            game.filled_tiles.append(self.tile)
            print(game)
        else:
            print("tile already picked")


class Undo(Action):
    def execute(self, game: Game):
        if game.marked_tiles() != 0:
            game.board[game.filled_tiles[-1]] = Mark._
            game.filled_tiles.pop()
            print(game)
        else:
            print("cant undo")


class FileStore(Action):
    def execute(self, game: Game):
        b = game.board
        with open("tiles", "wb") as f:
            pickle.dump(b, f)


class FileRead(Action):
    def execute(self, game: Game):
        with open("tiles", "rb") as f:
            listt = pickle.load(f)
            return listt


class FileDelete(Action):
    def execute(self, game: Game):
        file_path = "tiles"
        if os.path.exists(file_path):
            os.remove(file_path)
            print("File deleted...")


class main:
    game = Game()
    file_path = "tiles"
    if not os.path.exists(file_path):
        print(game)
    if os.path.exists(file_path):
        game.board = game.apply(FileRead())
        print(game)
    while True:
        input1 = int(input("pick a tile "))
        if input1 == -1:
            game.apply(Undo())
        elif input1 == -2:
            game.apply(FileStore())
            print("exiting out of the game...")
            break
        else:
            action = Update(tile=input1)
            game.apply(action)

        x_winner = game.is_winner("x")
        o_winner = game.is_winner("o")
        is_draw = game.is_draw()

        if x_winner:
            print("x is the winner")
            game.apply(FileDelete())
            break
        elif o_winner:
            print("o is the winner")
            game.apply(FileDelete())
            break
        elif is_draw:
            print("its a draw")
            game.apply(FileDelete())
            break
        else:
            game.apply(FileStore())


if __name__ == "__main__":
    main()
