

def minCoins(coins, m, V):
    res = 0
    test = V
    ans = []
    for i in range(m-1, -1, -1):
        while test >= coins[i]:
            test -= coins[i]
            res+=1
            ans.append(coins[i])
    return res




if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    m = len(coins)
    V = 13
    print("Minimum coins required is ",minCoins(coins, m, V))