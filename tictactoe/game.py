import abc
import enum
import dataclasses as dc


class Mark(enum.IntEnum):
    _ = 0
    x = 1
    o = 2

    def __repr__(self) -> str:
        return self._name_

    def __str__(self) -> str:
        return repr(self)


@dc.dataclass
class Game:
    moves: list["Pick"] = dc.field(default_factory=list)
    board: list[Mark] = dc.field(default_factory=lambda: [Mark._] * 9)

    def apply(self, action: "Action"):
        action.execute(self)

    def check(self) -> tuple[bool, Mark]:
        return True, Mark._

    def __repr__(self) -> str:
        b = self.board
        return f"""Board
        {" ".join(map(repr, b[0:3]))}
        {" ".join(map(repr, b[3:6]))}
        {" ".join(map(repr, b[6:9]))}
        """


class Action(abc.ABC):
    @abc.abstractmethod
    def execute(self, game: Game): ...


class Undo(Action):
    def execute(self, game: Game): ...


@dc.dataclass
class Pick(Action):
    tile: int

    def execute(self, game: Game):
        b = game.board
        n_marked_tiles = sum(Mark._ != _ for _ in b)
        n_even_marked_tiles = n_marked_tiles % 2 == 0
        b[self.tile] = Mark.x if n_even_marked_tiles else Mark.o


def main():
    game = Game()
    print(game)
    picks = [0, 3, 7, 1]
    picks = map(Pick, picks)
    for pick in picks:
        game.apply(pick)
        print(pick.tile)
        print(game)
        ended, winner = game.check()
        if ended:
            if w := winner:
                print(f"{w} won!")
            else:
                print("tie!")
            break


if __name__ == "__main__":
    main()
