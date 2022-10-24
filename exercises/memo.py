"""
Memory game

The game should: 
1.- Be able to be represented in an axis/board.
2.- Have at least 6 rows and 6 columns. 
3.- It can also generate randomly values that help stimulate memory.
4.- Have clear rules. 
5.- Must use concepts seen in the formation unit: decisions, loops, functions and Lists. 

"""
import random

def generate_board(n):
    """
    Function that will return the generated random board
    """

    #Generating a list of random values with only one duplicate of each element
    values = []
    for m in range(1, int((n**2)/2)+1):
        values.append(m)
        values.append(m)
    
    #Generating the board of the game
    board = []
    for i in range(n):
        row = []
        board.append(row)
        for j in range(n):
            rand_ind = random.randint(0, len(values)-1)
            row.append(values[rand_ind])
            values.pop(rand_ind)

    return board

def generate_eboard(n):
    #Generating an empty board in order to show that when the code is running
    e_board = []
    for i in range(n):
        e_row = []
        e_board.append(e_row)
        for j in range(n):
            e_row.append("-")
    return e_board


def print_board(board):
    """
    Function that prints any board 
    """
    "This function prints the board"
    for i in range(len(board)):
        print(f"{board[i]}\n")


def check_target(x,y,empty,board,save1):
    """This function returns if the player hitted a target"""
    #saving that value
    save2 = board[x][y]
    #reflect that value in the board
    empty[x][y] = save2 
    print_board(empty)
    if save2 == save1: 
        print("It's a match!!!")
        return True
    else: 
        print("Miss!!!")
        return False
    
            
def game(board, empty, answer):
    """
    This function returns the total amount of points of each player during the game
    """
    player1_count = 0
    player2_count = 0
    turn = 0
    save1 = 0
    while answer != "n":
        print_board(empty)
        print("Enter the x,y coordinates: ")
        x_1 = int(input("x: "))
        y_1 = int(input("y: "))
        if x_1 > len(board) - 1 or y_1 > len(board) - 1:
            print(f"The length of x or y is bigger than {len(board)-1} (board length) please type them again: ")
        else:
            #variable that storages the given value
            save1 = board[x_1][y_1]
            #reflect that value in the board
            empty[x_1][y_1] = save1
            #print the board with the reflected value
            print_board(empty)
            print("Enter another coordinate: ")
            x_2 = int(input("x: "))
            y_2 = int(input("y: "))
            # function that will return if the hit was a success 
            result = check_target(x_2,y_2,empty,board,save1)
            # if a match was found
            if result: 
                #check the turn and add points
                if turn % 2 == 0:
                    player1_count += 1
                else: 
                    player2_count += 1
            else:
                #Hide again the cards
                empty[x_1][y_1] = "-"
                empty[x_2][y_2] = "-"
            #Ending the game or not
            answer = input("Do you want to keep playing?(y/n): ")
            if answer != "n":
                #updating the turn
                turn += 1
            else: 
                return player1_count, player2_count

def score(result1, result2):
    """
    This function prints the final score of the game"""
    if result1 > result2: 
        print(f"¡The winner is player 1 with the score of: {result1} over {result2}!")
    elif result2 > result1: 
        print(f"¡The winner is player 2 with the score of: {result2} over {result1}!")
    else: 
        print(f"¡It's a draw!")
        print(f"Player 1 scored: {result1} points")
        print(f"Player 2 scored: {result2} points")

def main():
    """
    Main function of the code.
    """
    # Optional
    # n = int(input("Enter the size of the board: "))
    n = 6
    #Matching the board and the empty board as a result of the generate board function
    board = generate_board(n)
    empty = generate_eboard(n)
    print("Welcome to the memo game")
    answer = input("Enter \'y\' to start the game: ")
    #The total amount of points of each player
    result1, result2 = game(board, empty,answer)
    #Print the final results of the game
    score(result1, result2)
    print("Thanks for playing")

main()