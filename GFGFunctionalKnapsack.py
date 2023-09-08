
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight




class Solution:
    def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value/x.weight, reverse=True)
        tot = 0.0
        for i in range(n):
            if W == 0:
                break
            if arr[i].weight < W:
                tot+=arr[i].value
            else:
                x = arr[i].value/arr[i].weight
                x = x*W
                tot+=x
                break
            W-=arr[i].weight
        return tot



if __name__ == '__main__':
    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    obj = Solution()
    ans = obj.fractionalKnapsack(W, arr, n)
    print("The maximum value is", ans)