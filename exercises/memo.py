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
            

def main():
    """
    Main function of the code.
    """
    n = 20
    board = generate_board(n)
    print(board)

main()