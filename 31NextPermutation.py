# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# Examples
# Example 1 :

# Input format: Arr[] = {1,3,2}
# Output: Arr[] = {2,1,3}
# Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
# Example 2:

# Input format: Arr[] = {3,2,1}
# Output: Arr[] = {1,2,3}
# Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.


def nextGreaterPermutation(A):
    idx = -1
    for i in range(len(A)-2, -1, -1):
        if A[i] < A[i+1]:
            idx = i
            break
    if idx == -1:
        return A.reverse()
    for i in range(len(A) -1, idx, -1):
        print(A[i] > A[idx])
        if A[i] > A[idx]:
            A[i], A[idx] = A[idx], A[i]
            break
    A[idx+1:] = reversed(A[idx+1:])
    return A




if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")

