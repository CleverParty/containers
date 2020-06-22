import nashpy as nash
import numpy as np


A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
rockPaperScissors= nash.Game(A)
rockPaperScissors
print(rockPaperScissors)
sigma_r = [0, 0, 1]
sigma_c = [0, 1, 0]
print(rockPaperScissors[sigma_r, sigma_c])
# calculating nash equilibria 
equilibrium = rockPaperScissors.support_enumeration()
print("\nThe nash equilibrium values represented with payoffs :\n")
print(list(equilibrium))

# with random seed 
iterations = 100
np.random.seed(10)
count = rockPaperScissors.fictitious_play(iterations = iterations)
print("\nWith random seed generation for each actors (RPS) :\n")
for i, j in count:
    print(i, j)

# matching pennies : 
print("Matching pennies results below\n")
B = np.array([[1, -1], [-1, 1]]) # row player wins if both heads and coloumn player wins when both are tails
pennies = nash.Game(B)
print(pennies)

# prisoner's dilemma : 
print("Modified prisoner's dilemma\n")
C = np.array([[3, 0], [5, 1]])
D = np.array([[1,3], [0,0]])
dilemma = nash.Game(C,D)
dilemmaOne = nash.Game(A,C) # different combinations for different group of players
print(dilemma)
print("\n")
print(" \/ Modified equilibrium for rock paper scissors \/ \n")
print(dilemmaOne)
print("test git structure")