from random import randint
import sys
from colorama import Fore, Back, Style

board = []




for x in range(6):
    board.append(["O"] * 6)


def print_menu():
    print(Fore.GREEN +
    """\n
                              (          (        )  (    (     
   (     (       *   )  *   ) )\ )       )\ )  ( /(  )\ ) )\ )  
 ( )\    )\    ` )  /(` )  /((()/(  (   (()/(  )\())(()/((()/(  
 )((_)((((_)(   ( )(_))( )(_))/(_)) )\   /(_))((_)\  /(_))/(_)) 
((_)_  )\ _ )\ (_(_())(_(_())(_))  ((_) (_))   _((_)(_)) (_))   
 | _ ) (_)_\(_)|_   _||_   _|| |   | __|/ __| | || ||_ _|| _ \  
 | _ \  / _ \    | |    | |  | |__ | _| \__ \ | __ | | | |  _/  
 |___/ /_/ \_\   |_|    |_|  |____||___||___/ |_||_||___||_|  
 
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
    \n""")

    menu_handler()
    

def menu_handler(): ## To nie działa jeszcze wcale a wcale 

    user_choice = False
    if user_choice == False:
        number = input("""
                        What it will be Capitan? 
                            1. Start 
                            2. Quit
                            Choice: """)
        user_choice = choice(number)
    return number   

        # if number == 1:
        #     print("Let's play Capitan!")
        # elif number == 2:
        #     sys.exit()


def choice(user_input):

    if user_input == "1":
        print("Let's play Capitan!")
    if user_input == "2":
        sys.exit()
    else:
        if len(user_input) != 1 and user_input.isalpha():
            print("You need write one number!")
    return False


def print_board(board):
    print("1","2","3","4","5","6")

    for row in board:
        print((" ").join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


def turn_handler():
    for turn in range(11):
        print("Turn"), turn
        guess_row = int(input("Guess Row:"))
        guess_col = int(
            input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] =  "X"
        if turn == 10:
            print(Fore.RED + "Game Over")
        turn =+ 1
        print_board(board)

def main():
    print_menu()
    print_board(board)
    random_row(board)
    random_col(board)
    turn_handler()

if __name__ == "__main__":
   
    main()