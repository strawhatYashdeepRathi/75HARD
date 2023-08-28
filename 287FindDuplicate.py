# Find the duplicate in an array of N+1 integers
# Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number, your task is to find the duplicate number.

# Examples:

# Example 1: 

# Input: arr=[1,3,4,2,2]

# Output: 2



def findDuplicate(arr):
    # testHash = [0]*(len(arr) + 1)
    # for i in range(len(arr)):
    #     if (testHash[arr[i]] == 0):                     {********   HASHMAPS SOL have SC of O(N)            *************}
    #         testHash[arr[i]] +=1
    #     else:
    #         return arr[i]

    #   {*********  Linked List cycle methpd      *************}

    sp = 0
    fp = 0
    while True:
        sp = arr[sp]
        fp = arr[arr[fp]]
        if (sp == fp):
            break
    fp = 0
    while sp != fp:
        sp = arr[sp]
        fp = arr[fp]
    return fp



if __name__ == "__main__":
    arr = [1, 3, 4, 2, 2]
    print("The duplicate element is ", findDuplicate(arr))


