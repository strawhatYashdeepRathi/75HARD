# Median of Two Sorted Arrays of different sizes
# Problem Statement: Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays. The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.

# Examples
# Example 1:
# Input Format: n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
# Result: 3.5
# Explanation: The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.





def median(nums1, nums2):
    a, b= nums1, nums2
    if len(a) > len(b):
        a, b = b, a
    tot = len(a) + len(b)
    half = tot//2
    l, r = 0, len(a) - 1
    while True:
        m1 = (l + r) // 2
        m2 = half - m1 - 2
        aleft = a[m1] if m1>=0 else float('-infinity')
        aright = a[m1+1] if (m1+1) < len(a) else float ('infinity')
        bleft = b[m2] if m2>=0 else float('-infinity')
        bright = b[m2+1] if (m2+1)<len(b) else float('infinity')
        if aleft <= bright and bleft <= aright:
            if tot%2:
                return min(aright, bright)
            else:
                return (max(aleft, bleft) + min(aright, bright))/2
        elif aleft > bright:
            r = m1 - 1
        else:
            l = m1 + 1


a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print("The median of two sorted arrays is {:.1f}".format(median(a, b)))