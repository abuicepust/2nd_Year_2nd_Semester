import copy
import random
import numpy as np
def take_input():
    n = int(input("Enter the size of board : "))
    return n
def get_board(n):
    board = [["."]*n for i in range(n)]
    return board
def add_solution(board):
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)

def is_safe(board,row,col,n):
    for j in range(col):
        if(board[row][j] == "Q"):
            return False
    #check upper diagonal
    i,j=row,col
    while i>=0 and j>=0:
        if(board[i][j]=="Q"):
            return False
        i-=1
        j-=1
    #check for lower diagonal
    x,y=row,col
    while x<n and y>=0:
        if(board[x][y]=="Q"):
            return False
        x+=1
        y-=1
    return True



def solve (board,col,n):
    if(col >= n):
        return
    for i in range(n):
        if(is_safe(board,i,col,n)):
            board[i][col]="Q"
            if(col == n-1 ):
                add_solution(board)
                board[i][col]="."
                return
            solve(board,col+1,n) #recursive call
            #Backtrack
            board[i][col]="."

def print_solution(solutions,n):
    position = []
    x=random.randint(0,len(solutions)-1)
    array1=np.array(solutions[x])
    for i in range(len(array1)):
        for j in range(len(array1[0])):
            if(array1[i][j]=="Q"):
                position.append([i+1,j+1])
    print(f"Row and Column respect to queen position is : {position}")
    print(f"Total number of solution is {len(solutions)}")
    print("One of the solution is :")
    for row in solutions[x]:
        print(" ".join(row))


#Driver code
n=take_input()
board=get_board(n)
solutions=[]
solve(board,0,n)
print_solution(solutions,n)
