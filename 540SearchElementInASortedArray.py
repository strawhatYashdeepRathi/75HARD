
def singleNonDuplicate(arr):
  l = 0
  r = len(arr)-1
  if len(arr) == 1:
    return arr[0]
  while l <= r:
    mid = l + ((r-l)//2)
    if (mid-1 < 0 or arr[mid] != arr[mid-1]) and (mid+1 == len(arr) or arr[mid] != arr[mid+1]):
        return arr[mid]
    
    if ((mid%2 == 0 and arr[mid] == arr[mid+1]) or (mid%2 != 0 and arr[mid] == arr[mid-1])):
        l = mid+1
    else:
        r = mid-1


arr = [1, 1, 2, 2, 3]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)