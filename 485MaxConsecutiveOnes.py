from typing import List




class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        counter = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                counter+=1
                maxC = max(maxC, counter)
            else:
                counter = 0
        return maxC




if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    obj = Solution()
    ans = obj.findMaxConsecutiveOnes(nums)
    print("The maximum  consecutive 1's are", ans)