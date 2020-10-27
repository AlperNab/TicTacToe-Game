#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe Game 
# ##### Scratch Building
# ##### No GUI Required 

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[8]:


from IPython.display import clear_output

def display_board(board):
    print (board[0],'l',board[1],'l',board[2])
    print('------------')
    print (board[3],'l',board[4],'l',board[5])
    print('------------')
    print (board[6],'l',board[7],'l',board[8])
    print('------------')


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[9]:


test_board = ['1','2','3','4','5','6','7','8','9']
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[10]:


def player_input():
    p=input("Enter your name")
    p1=input("Enter your name")
    marker=input("Enter x or o")
    return marker
    pass


# **TEST Step 2:** run the function to make sure it returns the desired output

# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[11]:


def place_marker(board, marker, location):
    board[location-1]=marker.upper()
    pass


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[12]:


def check(board):
    markerr=board[location-1]
    
    #check rows
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
    


    


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[13]:


import random
def choose_first(board):
    x=random.randint(0,1)
    if x==0:
        print(p +" plays first")
        return 1
    else:
        print(p1 +" plays first")
        return 0


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[15]:


def space_check(board, location):
    if board[location-1]==" ":
        return True
    else: 
        return False


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[16]:


def full_board_check(board):
    x=False
    for i in range(9):
        if board[i]=="marker":
            x=False
            break
            print ("End Of the game")   
        elif board[i]=="i":
            return True
       
    


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[17]:


def player_choice(board):
    location=int(input("Enter next location"))
    board[location-1]=input("Enter your next letter").upper()
    space_check(board, location)
    pass


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[18]:


def replay():
    new_game= input("do you want to play again ,Enter True or false")  
    if new_game!= True or False:
        print("invalid input")
    pass


# In[19]:


def turn():
    print("your turn")


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


from IPython.display import clear_output
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


# In[ ]:





# ## Good Job!
