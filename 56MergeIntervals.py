
# Merge Overlapping Sub-intervals
# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

# Examples
# Example 1:
# Example 1: 

# Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

# Output: [[1,6],[8,10],[15,18]]

# Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
#  intervals.




def mergeOverlappingIntervals(intervals):
    n = len(intervals)
    intervals.sort()                                                                          #  TC ---> O(NlogN)
    res = []
    for i in range(n):
        if res and intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res
        



if __name__ == '__main__':
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = mergeOverlappingIntervals(arr)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()