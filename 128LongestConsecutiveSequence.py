# Longest Consecutive Sequence in an Array
# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

# Examples
# Example 1:

# Input: [100, 200, 1, 3, 2, 4]

# Output: 4


def longestSuccessiveElements(a):
    res = 0
    if len(a) == 0: return 0
    temp = set()
    for i in range(len(a)):
        temp.add(a[i])
    for ele in temp:
        cnt = 0
        if ele -1 not in temp:
            cnt+=1
            while ele+1 in temp:
                ele+=1
                cnt+=1
            res = max(res, cnt)
            
    return res

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)