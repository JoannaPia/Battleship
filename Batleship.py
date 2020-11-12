from random import randint
import sys

board = []

def start_game():

    print("""\n
                              (          (        )  (    (     
   (     (       *   )  *   ) )\ )       )\ )  ( /(  )\ ) )\ )  
 ( )\    )\    ` )  /(` )  /((()/(  (   (()/(  )\())(()/((()/(  
 )((_)((((_)(   ( )(_))( )(_))/(_)) )\   /(_))((_)\  /(_))/(_)) 
((_)_  )\ _ )\ (_(_())(_(_())(_))  ((_) (_))   _((_)(_)) (_))   
 | _ ) (_)_\(_)|_   _||_   _|| |   | __|/ __| | || ||_ _|| _ \  
 | _ \  / _ \    | |    | |  | |__ | _| \__ \ | __ | | | |  _/  
 |___/ /_/ \_\   |_|    |_|  |____||___||___/ |_||_||___||_|  

 |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\                             
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                     JP-SJ/
 \_________________________________________________________________________|


   \n                                                
    Hello everybody! You need choice game options to start the game.     
    You have to ship to put on the board: 
    1) Submarine    <---   size 2 - so it's two coordinate
    2) Patrol Boat  <--    size 1 - so it's one coordinate  
                        GOOD LUCK! """)


    #init_board(board)   

    choice = None
    while choice is None:
        while True:
            try:
                user_choice = int(input(
    """
    Choice which option you what to play:
    1 - Now you have two players
    2 - Player agains AI mode
    Your choice: """))
                break
            except ValueError:
                print("You need choice the number!")
                continue
        if user_choice > 0 and user_choice <=3:
            choice = True
        else:
            print("You need write the number from menu 1 or 2! Please Try again.")
    return choice    

def init_board(board): # it's empty board without any ship

    how_many_times = 1
    
    print("  1 2 3 4 5")
    for col in range(0,how_many_times):
        board.append(["A"] + ["O"]*5)

    for col in range(0,how_many_times):
        board.append(["B"]+ ["O"]*5)

    for col in range(0,how_many_times):
        board.append(["C"]+ ["O"]*5)

    for col in range(0,how_many_times):
        board.append(["D"]+ ["O"]*5)

    for col in range(0,how_many_times):
        board.append(["E"]+ ["O"]*5)

    for row in board:
        print(" ".join(row))


def mark(board, row, col):

    board[row][col] = input_player

def print_board(board): #print the board with the player input

    board = [["O","O","O","O","O"],["O","O","O","O", "O"],["O","O","O","O","O"],["O","O","O","O","O"],["O","O","O","O","O"]]


    print("  1 2 3 4 5")
    print("A",board[0][0],board[0][1],board[0][2],board[0][3],board[0][4])
    print("B",board[1][0],board[1][1],board[1][2],board[1][3],board[1][4])
    print("C",board[2][0],board[2][1],board[2][2],board[2][3],board[2][4])
    print("D",board[3][0],board[3][1],board[3][2],board[3][3],board[3][4])
    print("E",board[4][0],board[4][1],board[4][2],board[4][3],board[4][4])


def put_ship_by_player1(board):

    row, col = 0,0
    
    input_player = input("Give me the coordinate to put the first shipe: ") # put the ship with coordinate ?
    if input_player.upper() in board and board[input_player.upper()] == "O":
        board[input_player.upper()] = "X"
    mark(board, row, col)
    print_board(board)
                
            
    input_player = input()
    input_player = input_player.lower() # user can end the game
    if input_player == "quit":
        print("Goodbye~!")
        sys.exit()
    elif len(input_player) != 2:
        print("Give me the coordinate. For example A2, B5. Nothing more nothing less.")
        put_ship_by_player1(board)
    else: 
        row = input_player[0]
        col = int(input_player[1])-1
    
    if row == "A":
        row = 0
    elif row == "B":
        row = 1
    elif row == "C":
        row = 2
    elif row == "D":
        row = 3
    elif row == "E":
        row = 4

    if input_player not in ["A1","A2","A3","A4","A5",
                         "B1","B2","B3","B4", "B5",
                         "C1","C2","C3""C4","C5",
                         "D1","D2","D3""D4","D5",
                         "E1","E2","E3","E4","E5"]:
        print("You put the wrong coordinate: ")
        row,col = put_ship_by_player1(board)
    elif board[row][col] != "O":
        print("Your coordinate are the same. Put in the other place. ")
        row,col = put_ship_by_player1(board)

    return row, col


# def hide_row_ship(board):

#     return randint(0, len(board)-1) ## ??
    
# def hide_col_ship(board):

#     return randint(0, len(board[0])-1)  ## ??



def main():

    start_game()
    init_board(board)
    put_ship_by_player1(board)


if __name__ == "__main__":
   
    main()