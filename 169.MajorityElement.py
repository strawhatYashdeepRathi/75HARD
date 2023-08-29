# Find the Majority Element that occurs more than N/2 times
# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.

# Examples
# Example 1:
# Input Format: N = 3, nums[] = {3,2,3}
# Result: 3
# Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 


def majorityElement(arr):
    curr = None
    count = 0
    for i in range(len(arr)):
        if count == 0:
            curr = arr[i]
            count+=1
        elif arr[i] == curr:
            count+=1
        else:
            count-=1
    temp = 0
    for i in range(len(arr)):
        if arr[i] == curr:
            temp+=1
    if (temp > len(arr)/2):
        return curr
    
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)
