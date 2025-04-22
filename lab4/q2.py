from math import *

def countSquaresInBetween(nums):
    nums = nums.split(" ")
    nums = [int(i) for i in nums]
    start = ceil(sqrt(nums[0]))
    end =floor(sqrt(nums[1]))
    count = end-start+1
    
    return count
 
n = int(input("Enter the number of inputs: "))
for i in range(n):
    pair = input("\nEnter a number pair: ")
    print("Number of perfect squres in between: ", countSquaresInBetween(pair)) 


