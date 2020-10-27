import random

from IPython.display import clear_output

def display_board(board):
    print (board[0],'l',board[1],'l',board[2])
    print('------------')
    print (board[3],'l',board[4],'l',board[5])
    print('------------')
    print (board[6],'l',board[7],'l',board[8])
    print('------------')


test_board = ['1','2','3','4','5','6','7','8','9']
display_board(test_board)


def player_input():
    p=input("Enter your name")
    p1=input("Enter your name")
    marker=input("Enter x or o")
    return marker
    pass


def place_marker(board, marker, location):
    board[location-1]=marker.upper()
    pass


def check(board):
    markerr=board[location-1]
    def X():
        if board[0] == markerr and board[1]== markerr and board[2]== markerr :
            print(marker + " wins")
        elif board[3] == markerr and board[4]== markerr and board[5]== markerr :
            print(marker + " wins")
        elif board[6] == markerr and board[7]== markerr and board[8]== markerr :
            print(marker + " wins")
        #check columns    
        elif board[0] == markerr and board[3]== markerr and board[6]== markerr :
            print(marker + " wins")
        elif board[1] == markerr and board[4]== markerr and board[7]== markerr :
            print(marker + " wins")
        elif board[2] == markerr and board[5]== markerr and board[8]== markerr :
            print(marker + " wins")
        #check diagnols
        elif board[0] == markerr and board[4]== markerr and board[8]== markerr :
            print(marker + " wins")
        elif board[2] == markerr and board[4]== markerr and board[6]== markerr :
            print(marker + " wins")
    if markerr == "X":
        X()
    elif markerr=="O":
        O()


import random
def choose_first(board):
    x=random.randint(0,1)
    if x==0:
        print(p +" plays first")
        return 1
    else:
        print(p1 +" plays first")
        return 0


def space_check(board, location):
    if board[location-1]==" ":
        return True
    else: 
        return False

def full_board_check(board):
    x=False
    for i in range(9):
        if board[i]=="marker":
            x=False
            break
            print ("End Of the game")   
        elif board[i]=="i":
            return True


def player_choice(board):
    location=int(input("Enter next location"))
    board[location-1]=input("Enter your next letter").upper()
    space_check(board, location)
    pass


def replay():
    new_game= input("do you want to play again ,Enter True or false")  
    if new_game!= True or False:
        print("invalid input")
    pass

def turn():
    print("your turn")

print('Welcome to Tic Tac Toe!')


display_board(test_board)
p=input("Enter your name")
p1=input("Enter your name")
choose_first(test_board)
marker= input("Enter your choice").upper()
location= int(input("enter location"))
place_marker(test_board, marker, location)


while(True):
        if turn == p:
            place_marker(test_board, marker, location)
            display_board(test_board)
            player_choice(test_board)
            space_check(test_board, location)
            full_board_check(test_board)
            check(test_board)
            if check(test_board) == True:
                test_board = ['-','-','-','-','-','-','-','-','-']
                print(test_board)
            print(p1 + " turn")
        else:
            print(p1 + " turn")
            place_marker(test_board, marker, location)
            display_board(test_board)
            player_choice(test_board)
            space_check(test_board, location)
            full_board_check(test_board)
            check(test_board)
            if check(test_board) == True:
                test_board = ['-','-','-','-','-','-','-','-','-']
                print(test_board)
            print(p + " turn")

replay()
