

from typing import List




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def recursive(idx, sub):
            if idx == len(nums):
                res.append(sub[::])
                return
            #   for where we select an element
            sub.append(nums[idx])
            recursive(idx+1, sub)
            sub.pop()
            # for when we do not select
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
            recursive(idx+1, sub)
        recursive(0, [])
        return res



if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print(*ans)