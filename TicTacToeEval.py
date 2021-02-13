# Katon Minhas
# Homework 1 Problem 3
# Tic Tac Toe

import numpy as np


# print out a given board
def print_board(board):
    print(board[0][0], "  ", board[0][1], "  ", board[0][2], "\n",
          board[1][0], "  ", board[1][1], "  ", board[1][2], "\n",
          board[2][0], "  ", board[2][1], "  ", board[2][2], "\n")



#%% Initialize board arrays
board1 = np.array([[-1,0,1], [0,-1,0], [0,0,0]])
board2 = np.array([[-1,0,1], [0,0,0], [-1,0,0]])
board3 = np.array([[-1,0,1], [0,0,0], [0,0,0]])
board4 = np.array([[1,0,0], [0,-1,-1], [0,0,0]])
board5 = np.array([[0,0,0], [1,-1,0], [-1,0,0]])
board6 = np.array([[0,0,1], [0,-1,1], [-1,0,-1]])
board7 = np.array([[0,0,0], [0,-1,0], [0,0,0]])
board8 = np.array([[0,0,1], [0,0,0], [-1,0,0]])
board9 = np.array([[-1,0,1], [0,0,0], [-1,1,-1]])
board10 = np.array([[-1,0,0], [1,1,-1], [-1,0,0]])
board11 = np.array([[-1,0,1], [-1,0,0], [0,0,0]])
board12 = np.array([[-1,0,0], [0,0,0], [0,0,0]])
board13 = np.array([[-1,0,1], [0,0,0], [0,0,-1]])
board14 = np.array([[0,0,-1], [0,0,0], [0,0,0]])


# put boards into an array
board_arr = np.array([board1,board2,board3,board4,board5,board6,board7,board8,board9,board10,board11,board12,board13,board14])


# recommended for X player
# 17 13 16
# 12 18 11
# 15 10 14

# recommended for O player
# 6 4 6
# 4 8 4
# 6 4 6

# Fill up recommended priorities
# xRecs = np.array([[17,13,16], [12,18,11], [15,10,14]])
# oRecs = np.array([[8,4,7], [3,9,2], [6,1,5]])


def Evaluate(board):
    
    isDuplicate = True;
    
    while (isDuplicate == True):
    
        # fill up oRecs and xRecs with random priorities in their recommended range
        oSides = np.array([1,2,3,4])
        np.random.shuffle(oSides)
        
        oCorners = np.array([5,6,7,8])
        np.random.shuffle(oCorners)
        
        xSides = np.array([9,10,11,12])
        np.random.shuffle(xSides)
        
        xCorners = np.array([13,14,15,16])
        np.random.shuffle(xCorners)
        
        # Fill up recommended priorities
        xRecs = np.array([[xCorners[0],xSides[0],xCorners[1]], [xSides[1],18,xSides[2]], [xCorners[2],xSides[3],xCorners[3]]])
        oRecs = np.array([[oCorners[0],oSides[0],oCorners[1]], [oSides[1],9,oSides[2]], [oCorners[2],oSides[3],oCorners[3]]])
        
        
        # Get locations of Xs and Os
        boardOs = np.where(board == -1)
        boardXs = np.where(board == 1)
        
        # Initialize P array
        P = np.zeros((3,3))
        
        # Fill P array with X weights where X, O weights where O
        
        P[boardXs[0], boardXs[1]] = xRecs[boardXs[0], boardXs[1]]
        
        # if there are the same number of Xs and Os on the board, double Os weight
        if boardOs[0].size == boardXs[0].size:
            P[boardOs[0], boardOs[1]] = -2*oRecs[boardOs[0], boardOs[1]]
        else:
            P[boardOs[0], boardOs[1]] = -1*oRecs[boardOs[0], boardOs[1]]
        
        
        Eval = 0
        
        # Evaluate based on following algorithm:
        # if a row, column, or diagonal is a valid O line:
        #   Eval = Eval + (sum of recommended priority values)
        # if a row, column, or diagonal is a valid X line:
        #   Eval = Eval + (sum of recommended priority values)
        
        for i in range(3):
            
            currRow = P[i,:]
            
            # examine ith row - get number of Xs, and number of Os
            numXRow = sum(currRow > 0)
            numORow = sum(currRow < 0)
        
            # if no Xs and at least one O, then it is a valid O row
            if (numORow > 0) & (numXRow == 0):
                Eval = Eval + sum(currRow)
            # if no Os and at least one X, then it is a valid X row
            elif (numXRow > 0) & (numORow == 0):
                Eval = Eval + sum(currRow)
            
            
            # Same process for ith column
            currCol = P[:,i]
            
            # examine ith row - get number of Xs, and number of Os
            numXCol = sum(currCol > 0)
            numOCol = sum(currCol < 0)
        
            # if no Xs and at least one O, then it is a valid O row
            if (numOCol > 0) & (numXCol == 0):
                Eval = Eval + sum(currCol)
            # if no Os and at least one X, then it is a valid X row
            elif (numXCol > 0) & (numOCol == 0):
                Eval = Eval + sum(currCol)
        
        
        # Evaluate diagonals
        diag1 = P[[0,1,2],[0,1,2]]
        diag2 = P[[2,1,0],[0,1,2]]
        
        numXdiag1 = sum(diag1 > 0)
        numXdiag2 = sum(diag2 > 0)
        
        numOdiag1 = sum(diag1 < 0)
        numOdiag2 = sum(diag2 < 0)
        
        # if no Xs and at least one O, then diag1 is a valid O diagonal
        if (numOdiag1 > 0) & (numXdiag1 == 0):
            Eval = Eval + sum(diag1)
        # if no Os and at least one X, then diag1 is a valid X diagonal
        elif (numXdiag1 > 0) & (numOdiag1 == 0):
            Eval = Eval + sum(diag1)
        
        # if no Xs and at least one O, then diag2 is a valid O diagonal
        if (numOdiag2 > 0) & (numXdiag2 == 0):
            Eval = Eval + sum(diag2)
        # if no Os and at least one X, then diag1 is a valid X diagonal
        elif (numXdiag2 > 0) & (numOdiag2 == 0):
            Eval = Eval + sum(diag2)
        
        
        # if duplicates, run again with new priorities
        if sum(Eval == Evaluations) != 0:
            isDuplicate = True
        else:
            return Eval
    

Evaluations = np.zeros(14)

for i in range(14):
    Evaluations[i] = Evaluate(board_arr[i])
    print("Board", i+1, " = ", Evaluations[i])


