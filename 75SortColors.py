# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

# Examples
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Input: nums = [0]
# Output: [0]

#      {********      Dutch National Flag Algo     *********}


def sortArray(nums):
    l = 0
    m = 0
    h = len(nums) -1
    while m <=h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            m+=1
            l+=1
        elif nums[m] == 1:
            m+=1
        else:
            nums[m], nums[h] = nums[h], nums[m]
            h-=1




n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()

