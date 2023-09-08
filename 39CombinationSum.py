

from typing import List




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, sub, tot):
            if tot == target:
                res.append(sub.copy())
                return
            if idx >= len(candidates) or tot > target:
                return
            sub.append(candidates[idx])
            dfs(idx, sub, tot+candidates[idx])
            sub.pop()
            dfs(idx+1, sub, tot)
        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()