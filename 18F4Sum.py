# 4 Sum | Find Quads that add up to a target value
# Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.

# Pre-req: 3-sum problem and 2-sum problem

# Note:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# arr[a] + arr[b] + arr[c] + arr[d] == target

# Examples
# Example 1:
# Input Format: arr[] = [1,0,-1,0,-2,2], target = 0
# Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Explanation: We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. The result obtained is such that the sum of the quadruplets yields 0.


def fourSum(nums, target):
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if (j> i+1 and nums[j] == nums[j-1]):
                continue
            l = j+1
            h = n-1
            while l < h:
                test_sum = nums[i] + nums[j] + nums[l] + nums[h]
                if (target == test_sum):
                    pair = [nums[i], nums[j], nums[l], nums[h]]
                    res.append(pair)
                    l+=1
                    h-=1
                    while l < h and nums[l] == nums[l-1]:
                        l+=1
                    while l < h and nums[h] == nums[h+1]:
                        h-=1
                elif (target < test_sum):
                    h-=1
                else :
                    l+=1
    return res




if __name__ == '__main__':
    nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target = 9
    ans = fourSum(nums, target)
    print("The quadruplets are:", ans)
    
