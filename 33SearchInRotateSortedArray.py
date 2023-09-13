# Search Element in a Rotated Sorted Array
# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

# Examples
# Example 1:
# Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
# Result: 4
# Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.


def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l+(r-l)//2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[l]:
            if target > nums[mid] or target < nums[l]:
                l = mid+1
            else:
                r = mid-1
        else:
            if target < nums[mid] or target > nums-r:
                r = mid-1
            else:
                l = mid+1
    return -1


if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)