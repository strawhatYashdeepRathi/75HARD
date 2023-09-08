

from typing import List


class Solution:
    def subsetSums(self, arr: List[int], n: int) -> List[int]:
        ans = []
        def recurSub(idx, summ):
            if idx == n:
                ans.append(summ)
                return

            #  if element gets selected
            recurSub(idx+1, summ+arr[idx])
            #  if element doesn't get selected
            recurSub(idx+1, summ)
        recurSub(0, 0)
        ans.sort()
        return ans


if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = Solution().subsetSums(arr, len(arr))
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()