board = ["", "", "", "", "", "", "", "", ""]
positions1 = [i for i in range(0, 3, 1)]
positions2 = [i for i in range(3, 6, 1)]
positions3 = [i for i in range(6, 9, 1)]
positions4 = [i for i in range(0, 7, 3)]
positions5 = [i for i in range(1, 8, 3)]
positions6 = [i for i in range(2, 9, 3)]
positions7 = [i for i in range(0, 9, 4)]
positions8 = [i for i in range(2, 7, 2)]
winning_positions = [positions1, positions2, positions3, positions4, positions5, positions6, positions7, positions8]

def play():
    chances = 1
    while chances <= 3:
        person1 = int(input("player1, enter the board number from 0-8 "))

        if board[person1] == "":
            board[person1] = "x"
            print()
            print(f"| {board[0]}  |  {board[1]}  |  {board[2]} |")
            print(f"| {board[3]}  |  {board[4]}  | {board[5]} |")
            print(f"| {board[6]}  |  {board[7]}  | {board[8]} |")
            print()
        else:
            print("choose another box, its filled already!")
        
        if chances == 3:
            board_row = []
            for positions in winning_positions:
                for position in positions:
                    board_row.append(board[position])
                if board_row.count('x') == 3:
                    return print("the winner is player1")
                board_row = []


        person2 = int(input("player2, enter the board number from 0-8 "))

        if board[person2] == "":
            board[person2] = "o"
            print()
            print(f"| {board[0]}  |  {board[1]}  |  {board[2]} |")
            print(f"| {board[3]}  |  {board[4]}  | {board[5]} |")
            print(f"| {board[6]}  |  {board[7]}  | {board[8]} |")
            print()
        else:
            print("choose another box, its filled already!")

        if chances == 3:
            board_row = []
            for positions in winning_positions:
                for position in positions:
                    board_row.append(board[position])
                if board_row.count('o') == 3:
                    return print("the winner is player2")
                board_row = []

        chances += 1


play()



