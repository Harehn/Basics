import random


# PROBLEM 1
def findMaxConsecutiveOnes(nums):
    return max([len(i) for i in ("".join([str(j) for j in nums])).split("0")])


def solvefindMaxConsecutiveOnes():
    print("PROBLEM 1")
    ll = [random.randint(0, 1) for i in range(15)]
    print(ll)
    print("Number of consecutive ones: ", findMaxConsecutiveOnes(ll))

# PROBLEM 2
def findNumbersWithEvenNumberOfDigits(nums):
    return len([i for i in nums if (len(str(i)) % 2) == 0])

def solvefindNumbersWithEvenNumberOfDigits():
    print("\nPROBLEM 2")
    ll = [random.randint(0, 1000000) for i in range(15)]
    print(ll)
    print("Number of numbers with even digits: ", findNumbersWithEvenNumberOfDigits(ll))

# PROBLEM 3
def getOrderedSquares(nums):
    return sorted([i * i for i in nums])

def solvegetOrderedSquares():
    print("\nPROBLEM 3")
    ll = sorted([random.randint(-100, 100) for i in range(15)])
    print("Ordered original List: ", ll)
    print("Ordered list pf squared: ", getOrderedSquares(ll))

solvefindMaxConsecutiveOnes() # PROBLEM 1
solvefindNumbersWithEvenNumberOfDigits() # PROBLEM 2
solvegetOrderedSquares() # PROBLEM 3
