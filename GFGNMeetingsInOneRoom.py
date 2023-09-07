# N meetings in one room
# There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

# Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


# Example 1:

# Input:
# N = 6
# start[] = {1,3,0,5,8,5}
# end[] =  {2,4,6,7,9,9}
# Output: 
# 4

from typing import List

# class meeting:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

class Solution:


    def maxMeetings(self, s: List[int], e: List[int], n: int) -> None:
        hashh = [(s[i], e[i]) for i in range(n)]
        hashh.sort(key=lambda x: x[1])
        count = 1
        last = hashh[0][1]
        for i in range(1, n):
            if hashh[i][0] > last:
                count+=1
                last = hashh[i][1]
            
        return count


if __name__ == "__main__":
    obj = Solution()
    n = 8
    start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
    print(obj.maxMeetings(start, end, n))
