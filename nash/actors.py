import nashpy as nash
import numpy as np

def rPS(flag):
    A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
    if( flag == 'normal' ):
        rockPaperScissors = nash.Game(A)
        sigma_r = [0, 0, 1]
        sigma_c = [0, 1, 0]
        print(rockPaperScissors[sigma_r, sigma_c])
        # calculating nash equilibria 
        # equilibrium = rockPaperScissors.support_enumeration()
        print("\nThe nash equilibrium values represented with payoffs :\n")
        # convert equillibrium to list type to print
        # with random seed 
    elif( flag == 'random' ):
        iterations = 100
        np.random.seed(10)
        rockPaperScissors = nash.Game(A)
        count = rockPaperScissors.fictitious_play(iterations = iterations)
        print("\nWith random seed generation for each actors (RPS) :\n")
        for i, j in count:
            print(i, j)

def matchingPennies():
    # matching pennies : 
    print("Matching pennies results below\n")
    B = np.array([[-1, -1], [-1, 1]]) # row player wins if both heads and coloumn player wins when both are tails
    pennies = nash.Game(B)
    return pennies

def prisonersDilemma(matrixA,matrixB):
    # prisoner's dilemma : 
    print("Modified prisoner's dilemma\n")
    C = np.array([matrixA[0], matrixA[1]])
    D = np.array([matrixB[0], matrixB[1]])
    dilemma = nash.Game(C,D)
    return dilemma


print("test git structure")
rPS('normal')
matrixA = [[3,0], [5,1]]
matrixB = [[1,3], [0,0]]
prisonersDilemma(matrixA,matrixB)