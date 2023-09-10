from typing import List




class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        res = ""
        nums = []
        for i in range(1, n):
            nums.append(i)
            fact*=i
        nums.append(n)
        k-=1
        while True:
            res+=str(nums[k//fact])
            nums.pop(k//fact)
            if not nums:
                break
            k%=fact
            fact//=len(nums)
        return res





if __name__ == "__main__":
    n = 3
    k = 3
    obj = Solution()
    ans = obj.getPermutation(n, k)
    print("The Kth permutation sequence is", ans)