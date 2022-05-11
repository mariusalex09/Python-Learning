from numpy import random
import numpy as np

x = random.randint(100)
print(x)  # generate random number until 100

x = random.rand(1) #generates random float form 0 to 1
print(x)

#generate a 1D array with 5 random integers from 0 to 100
x = random.randint(100, size = (5))
print(x) #[54 93 96  7  8]

#generate 2D array with 3 rows and 5 columns
x = random.randint(100, size = (3, 5))
print(x)
"""
[[31 50 63 75 82]
 [20 49 33 15 22]
 [81 10 80 24 53]]
"""

#generate 1D array with float values
x = random.rand(5)
print(x) #[0.44707288 0.80748822 0.48564378 0.63751562 0.02831694]

#or 2D array with float values
x = random.rand(3, 5)
print(x)
"""
[[0.79806999 0.92595873 0.66580865 0.46483435 0.90285271]
 [0.05836392 0.40411097 0.2685779  0.97329057 0.02675323]
 [0.31080998 0.40546442 0.49083167 0.50289244 0.88007273]]
"""

#choice() method allows to generate a random value based on an array of values; takes the array as parameter and returns one of the values
x = random.choice([3, 5, 7, 9])
print(x) #e.g. 7

#choice() allows also returnal of an array by specifying the size
x = random.choice([3, 5, 7, 9], size = (3, 5))
print(x)
"""
[[7 7 3 3 7]
 [9 3 5 7 9]
 [9 7 9 9 5]]
"""

#Data distribution - is a list of all possible values and how often each value occurs
#Such lists are important for statistics and data science
#the Random module offers methods that return randomly generated data distributions

#a random distribution is a set of random numbers that follows a certain probability density function
# the choice() method allows to specify the probability for each value; the probability is between 0 and 1

#generate 1D array with 100 values where each value has to be 5,5,7 or 9
x = random.choice([3, 5, 7, 9], p = [0.1, 0.3, 0.6, 0.0], size = (100))  #p indicates the probability for each elementS
print(x)
"""
[3 5 7 5 7 3 5 7 7 7 7 7 5 7 5 7 7 7 7 7 5 7 5 7 5 5 7 7 7 5 7 7 7 7 5 7 7
 7 7 7 7 7 7 5 7 7 7 3 7 7 7 7 3 3 3 7 7 5 7 3 7 5 7 7 5 7 5 7 7 7 3 7 5 5
 7 7 7 7 7 7 7 7 5 5 7 7 7 7 7 7 7 5 5 3 5 5 7 7 7 7]
"""

#permutations with suffle() and permutation() methods
#randomly suffle elements of array
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)  #[2 5 1 3 4]  the shuffle() method suffles the original array so it changes it

#generate permutations
arr = np.array([1,2,3,4,5])
print(random.permutation(arr)) # [5 3 2 4 1] the permutation() method returns a re-arranged array and leaves the original unchanged


