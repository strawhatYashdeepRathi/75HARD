

from typing import List




def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()
    def backtrack(sub, idx, target):
        if target == 0:
            res.append(sub[::])
        if target <= 0:
            return
        prev = -1
        for i in range(idx, len(candidates)):
            if candidates[i] == prev:
                continue
            sub.append(candidates[i])
            backtrack(sub, i+1, target-candidates[i])
            sub.pop()
            prev = candidates[i]
    backtrack([], 0, target)
    return res





if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationSum2(v, 8)
    print(*comb)