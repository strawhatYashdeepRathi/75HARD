

# What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

# Examples
# Example 1:
# Input Format: N = 5, array[] = {1,2,3,4,5}
# Result: 0
# Explanation: we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.
import math

def merge(a, l, m, h):
    res_arr = []
    t = 0
    lp = l
    rp = m+1
    while lp <= m and rp <= h:
        if (a[lp]> a[rp]):
            t = t + (m-lp +1)
            res_arr.append(a[rp])
            rp+=1
        else:
            res_arr.append(a[lp])
            lp+=1
    while lp < m+1:
        res_arr.append(a[lp])
        lp+=1
    while rp < h:
        res_arr.append(a[rp])
        rp+=1
    for i in range(l, h + 1):
        a[i] = res_arr[i - l]
    return t



def mergeSort(a, l, h):
    count = 0
    if l >= h:
        return count
    m = math.floor((l + h)/2)
    count += mergeSort(a, l, m)
    count += mergeSort(a, m+1, h)
    count += merge(a, l, m, h)
    return count



def numberOfInversions(a, n):
    return mergeSort(a, 0, n-1)




if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    cnt = numberOfInversions(a, n)
    print("The number of inversions are:", cnt)

