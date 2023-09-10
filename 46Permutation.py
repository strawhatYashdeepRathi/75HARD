
from typing import List




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, nums):
            if (idx == len(nums)):
                res.append(nums[::])
                return 
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx+1, nums)
                nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(0, nums)
        return res



if __name__ == "__main__":
    obj = Solution()
    v = [1, 2, 3]
    sum = obj.permute(v)
    print("All Permutations are ")
    for i in range(len(sum)):
        for j in range(len(sum[i])):
            print(sum[i][j], end=" ")
        print()