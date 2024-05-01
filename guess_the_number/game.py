import random
import dataclasses as dc


@dc.dataclass
class Game:
    no_of_choices: int = dc.field(default=0)

    def guessing_number(self, actual_number, guessed_number) -> bool:
        if actual_number > guessed_number:
            print("the guess is too low")
            self.no_of_choices += 1
        elif actual_number < guessed_number:
            print("the guess is too high")
            self.no_of_choices += 1
        else:
            print(f"yes the number is {guessed_number}")
            print(f"the number of chances you used {self.no_of_choices + 1}")
            return True


def main():
    user_input = input("Enter a number range to guess! ")
    both_numbers = user_input.split("-")
    first_number = int(both_numbers[0])
    second_number = int(both_numbers[1])
    actual_number = random.randint(first_number, second_number)
    game = Game()
    while True:
        user_input1 = int(
            input(f"guess the number between {first_number} and {second_number} ")
        )
        res = game.guessing_number(actual_number, user_input1)
        if res:
            break


if __name__ == "__main__":
    main()
