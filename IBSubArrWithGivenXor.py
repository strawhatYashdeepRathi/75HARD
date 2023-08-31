# Count the number of subarrays with given xor K
# Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.

# Pre-requisite: Find the number of subarrays with the sum K

# Examples
# Example 1:
# Input Format: A = [4, 2, 2, 6, 4] , k = 6
# Result: 4
# Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

from collections import defaultdict

def subarraysWithXorK(A, B):
    count = 0
    xor = 0
    tmap = defaultdict(int)
    tmap[xor] +=1
    for i in range(len(A)):
        # calculate current XOR
        xor = xor ^ A[i]
        # calculate x 
        x = xor ^ B
        # count increases if x in map
        count+=tmap[x]
        # add current xor and its count to map
        tmap[xor]+=1
    return count



if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysWithXorK(a, k)
    print("The number of subarrays with XOR k is:", ans)