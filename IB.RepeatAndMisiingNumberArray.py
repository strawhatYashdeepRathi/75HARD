

# Find the repeating and missing numbers
# Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

# Examples
# Example 1:
# Input Format:  array[] = {3,1,2,5,3}
# Result: {3,4)
# Explanation: A = 3 , B = 4 
# Since 3 is appearing twice and 4 is missing



def findMissingRepeatingNumbers(a):
    n = len(a)
    SR = (n*(n+1))//2                # sum of all elements upto n 
    SR2 = (n*(n+1)*(2*n+1))//6       # sum of square of all elements upto n 
    S = 0
    S2 = 0
    for i in range(n):
        S+=a[i]
        S2+=(a[i]*a[i])

    val1 = S - SR   #  x-y
    val2 = S2 - SR2    #   x^2 - y^2  => (x-y)(x+y)
    val2 = val2 // val1     #   gets equation    => Find X+Y = (X^2-Y^2)/(X-Y):
    x = (val1 + val2)//2
    y = x - val1

    return [x, y]





if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbers(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")