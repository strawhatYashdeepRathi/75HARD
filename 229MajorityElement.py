# Majority Elements(>N/3 times) | Find the elements that appears more than N/3 times in the array
# Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.

# Pre-requisite: Majority Element(>N/2 times)

# Examples
# Example 1:
# Input Format: N = 5, array[] = {1,2,2,3,2}
# Result: 2
# Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

def majorityElement(arr):
    cnt1, cnt2 = 0, 0
    ele1, ele2 = None, None
    res_arr = []
    test = int(len(arr) / 3) + 1
    for i in range(len(arr)):
        if (cnt1 == 0 and arr[i] != ele2):
            ele1 = arr[i]
            cnt1 += 1
        elif (cnt2 == 0 and arr[i] != ele1):
            ele2 = arr[i]
            cnt2 += 1
        elif (ele1 == arr[i]):
            cnt1+=1
        elif (ele2 == arr[i]):
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    temp1, temp2 = 0, 0
    for i in range(len(arr)):
        if arr[i] == ele1:
            temp1+=1
        if arr[i] == ele2:
            temp2+=1
    if temp1 >= test:
        res_arr.append(ele1)
    if temp2 >= test:
        res_arr.append(ele2)
    
    return res_arr


arr = [11, 33, 33, 11, 33, 11]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()