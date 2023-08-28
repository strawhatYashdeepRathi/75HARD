# Merge two Sorted Arrays Without Extra Space
# Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

# Examples
# Example 1:

# Input: 
# n = 4, arr1[] = [1 4 8 10] 
# m = 5, arr2[] = [2 3 9]

# Output: 
# arr1[] = [1 2 3 4]
# arr2[] = [8 9 10]

# Explanation:
# After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.




def merge(nums1, nums2, m, n):
    
    l = m-1
    r = n-1
    entry_idx = m+n-1

    while r>=0:
        if l>=0 and nums1[l] > nums2[r]:
            nums1[entry_idx] = nums1[l]
            l-=1
        else:
            nums1[entry_idx] = nums2[r]
            r-=1
        entry_idx-=1
    print(nums1)

    # left_p = m-1
    # right_p = 0
    # while left_p >=0 and right_p < n:
    #     if (nums1[left_p] > nums2[right_p]):
    #         nums1[left_p], nums2[right_p] = nums2[right_p], nums1[left_p]
    #         left_p-=1
    #         right_p+=1
    #     else:
    #         break
    # nums1 = sorted(nums1[:m]) + nums1[m:]
    # nums2.sort()
    # for i in range(m, len(nums1)):
    #     print(i)
    #     nums1[i] = nums2[i-m]
    # print(nums1, nums2)







if __name__ == '__main__':
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]
    m = 3
    n = 3
    merge(arr1, arr2, m, n)

    # print("The merged arrays are:")
    # print("arr1[] = ", end="")
    # for i in range(m):
    #     print(arr1[i], end=" ")
    # print("\narr2[] = ", end="")
    # for i in range(n):
    #     print(arr2[i], end=" ")
    # print()


