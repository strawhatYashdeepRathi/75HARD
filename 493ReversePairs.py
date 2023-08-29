# Count Reverse Pairs
# Problem Statement: Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].

# Examples
# Example 1:

# Input: N = 5, array[] = {1,3,2,3,1)

# Output: 2 

# Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.


def mergeArr(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <=mid and right <=high:
        if arr[left] > arr[right]:
            temp.append(arr[right])
            right+=1
        else:
            temp.append(arr[left])
            left+=1
    while left <=mid:
        temp.append(arr[left])
        left+=1
    while right <=high:
        temp.append(arr[right])
        right+=1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]



def check(arr, low, mid, high):
    cnt = 0
    l = low
    r = mid+1
    for i in range(low, mid+1):
        while r <= high and arr[i] > 2*arr[r]:
            r+=1
        cnt+=(r-(mid+1))
    return cnt
        

def mergeSort(arr, low, high):
    count = 0
    if (low >= high):
        return count
    mid = (high + low)//2
    count+=mergeSort(arr, low, mid)
    count+=mergeSort(arr, mid+1, high)
    count+=check(arr, low, mid, high)
    mergeArr(arr, low, mid, high)
    return count

def team(skill: [int], n: int) -> int:
    return mergeSort(skill, 0, n - 1)

if __name__ == "__main__":
    a = [4, 1, 2, 3, 1]
    n = 5
    cnt = team(a, n)
    print("The number of reverse pair is:", cnt)

