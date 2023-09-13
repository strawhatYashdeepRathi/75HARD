
def NthRoot(N, M):
    def test(m):
        res = 1
        for i in range(N):
            res*=m
            if res > M:
                return 2
        if res == M:
            return 1
        return 0
    l, h = 0, M
    while l<=h:
        mid = (l+h)//2
        mm = test(mid)
        if mm == 1:
            return mid
        elif mm == 2:
            h = mid-1
        else:
            l = mid+1
    return -1


n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)