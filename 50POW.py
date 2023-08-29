# Implement Pow(x,n) | X raised to the power N
# Problem Statement: Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).

# Examples:

# Example 1:

# Input: x = 2.00000, n = 10

# Output: 1024.00000

# Explanation: You need to calculate 2.00000 raised to 10 which gives ans 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3

# Output: 9.26100

# Explanation: You need to calculate 2.10000 raised to 3 which gives ans 9.26100


def myPow(x, n):
    # ans = x
    # for i in range(n-1):               {*********       this wpont work for -ves        ***********}
    #     ans*=x
    # return ans

    res = 1.0
    temp_pow = n
    if temp_pow <0: temp_pow*=-1
    while temp_pow:
        if (temp_pow % 2 != 0):
            res*=x
            temp_pow-=1
        else:
            x*=x
            temp_pow = temp_pow//2
    if n<0: return 1.0/res
    return res


if __name__ == "__main__":
    print(myPow(2.00000, -2))