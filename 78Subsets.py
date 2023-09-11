from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurr(idx, sub):
            if idx == len(nums):
                res.append(sub[::])
                return
            # if item gets picked
            sub.append(nums[idx])
            recurr(idx+1, sub)
            sub.pop()
            # if not picked
            recurr(idx+1, sub)

        recurr(0, [])
        return res
    
solution = Solution()
nums = [1, 2, 3]
result = solution.subsets(nums)
print(result)