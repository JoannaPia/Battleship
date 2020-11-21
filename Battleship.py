from random import randint
import sys
import os
from colorama import Fore, Back, Style

class Parameters:
    red = '\033[91m'
    yellow = '\033[93m'
    green = '\033[92m'

    # def change_color(self, color, text):
    #     return color + text + Parameters.reset


board = []

for x in range(5):
    board.append(["O"] * 5)


def print_menu():
    print(Fore.BLUE +
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
    You have ten moves to win. Good lucky!
    \n""")

 

def menu_handler(): ## To nie działa jeszcze wcale a wcale 

    user_choice = False
    if user_choice == False:
        number = input("""
                        What it will be Capitan? 
                            1. Start 
                            2. Quit
                            Choice: """)

    if number == "1":
        print("Let's play Capitan!")
    if number == "2":
        sys.exit()
    else:
        if len(number) != 1 or number.isalpha():
            print("You need write one number!")
    return False


def print_board(board):
    print(" ","1","2","3","4","5")

    for i, row in enumerate(board, 1):
        print( i, (" ").join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


def turn_handler():


    for turn in range(11):
        turn = 0
        print("Turn" + " " + str(turn))
        guess_row = int(input("Guess Row:"))
        guess_col = int(
            input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] =="X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "M"
        if turn == 10:
            print("Game Over")
        turn =+ 1
        print_board(board)
    

def ask_yes_no(question):

    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()
    return response

def question_start_game():

    computer_question = ask_yes_no("Do you want play again? Answer yes or no:")
    
    if computer_question == "yes":
        print("You will start the game.")
        os.system("cls || clear")
        main()
    elif computer_question == "no":
        print("See you soon")
        sys.exit()
        

def main():

    print_menu()
    menu_handler()
    print_board(board)
    random_row(board)
    random_col(board)
    turn_handler()
    question_start_game()
    

if __name__ == "__main__":
   
    main()
    