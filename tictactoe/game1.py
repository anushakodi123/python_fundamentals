import enum
import io
import abc
import dataclasses as dc
import sqlite3
# import json


class Mark(enum.IntEnum):
    _ = 0
    x = 1
    o = 2

    def __repr__(self) -> str:
        return self._name_

    def __str__(self) -> str:
        return self._name_


@dc.dataclass
class Game:
    board: list = dc.field(default_factory=lambda: [Mark._ for _ in range(9)])
    filled_tiles: list = dc.field(default_factory=list)

    def __repr__(self) -> str:
        b = self.board
        return f"""Board
        {" ".join(map(repr, b[0:3]))}
        {" ".join(map(repr, b[3:6]))}   
        {" ".join(map(repr, b[6:9]))}
        """

    def is_winner(self, player: Mark) -> bool:
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


@dc.dataclass
class Update(Action):
    tile: int

    def execute(self, game: Game):
        b = game.board
        if b[self.tile] == Mark._:
            no_of_marked_tiles = game.marked_tiles()
            n_even_marked_tiles = no_of_marked_tiles % 2 == 0
            b[self.tile] = Mark.x if n_even_marked_tiles else Mark.o
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


class StorageDriver(abc.ABC):
    @abc.abstractmethod
    def store_move(self, update: Update): ...
    @abc.abstractmethod
    def read_moves(self) -> list[Update]: ...
    @abc.abstractmethod
    def undo_move(self): ...
    def delete_moves(self): ...


@dc.dataclass
class StoreDB(StorageDriver):
    def __post_init__(self):
        self.con = sqlite3.connect("tictactoe.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS moves(id INTEGER PRIMARY KEY, tile INTEGER)"
        )
        self.con.commit()

    def store_move(self, update: Update):
        self.cur.execute("INSERT INTO moves(tile) VALUES (?)", (update.tile,))
        self.con.commit()

    def read_moves(self) -> list[Update]:
        res = self.cur.execute("SELECT tile FROM moves")
        moves = res.fetchall()
        print("fetchingg", moves)
        print("listttt", [Update(move[0]) for move in moves])
        return [Update(move[0]) for move in moves]

    def undo_move(self):
        self.cur.execute("DELETE FROM moves WHERE id = (SELECT MAX(id) FROM moves)")
        self.con.commit()

    def delete_moves(self):
        self.cur.execute("DELETE FROM moves")
        self.con.commit()


@dc.dataclass
class DBUpdate(Action):
    sd: StoreDB
    update: Update

    def execute(self, game: Game):
        self.sd.store_move(self.update)
        self.update.execute(game)


@dc.dataclass
class DBUndo(Action):
    sd: StoreDB
    undo: Undo

    def execute(self, game: Game):
        self.sd.undo_move()
        self.undo.execute(game)


def main():
    game = Game()

    sd = StoreDB()
    for update in sd.read_moves():
        game.apply(update)

    while True:
        input1 = int(input("pick a tile "))
        if input1 == -1:
            action = DBUndo(sd, Undo())
        else:
            action = DBUpdate(sd, Update(tile=input1))
        game.apply(action)
        if game.is_winner(Mark.x):
            print("x is the winner")
            sd.delete_moves()
            break
        elif game.is_winner(Mark.o):
            print("o is the winner")
            sd.delete_moves()
            break
        elif game.is_draw():
            print("its a draw")
            sd.delete_moves()
            break


if __name__ == "__main__":
    main()
