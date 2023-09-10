
from typing import List




class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pal = []
        def testPal(str, l, r):
            while l<r:
                if str[l] != str[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(idx):
            if idx >= len(s):
                res.append(pal[::])
                return
            for i in range(idx, len(s)):
                if testPal(s, idx, i):
                    pal.append(s[idx:i+1])
                    dfs(i+1)
                    pal.pop()
        dfs(0)
        return res





if __name__ == "__main__":
    s = "aabb"
    obj = Solution()
    ans = obj.partition(s)
    print("The Palindromic partitions are :-")
    print(" [ ", end="")
    for i in ans:
        print("[ ", end="")
        for j in i:
            print(j, end=" ")
        print("] ", end="")
    print("]")