# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


# following sliding window

def solve(str):
    store = {}
    l = 0
    max_len = 0
    for i in range(len(str)):
        # case 1 - if curr character not in dictionary
        if str[i] not in store:
            max_len = max(max_len, i-l+1)
        # case 2 - our current window is [l:i], suppose string - abcdccb where l is at 3 and i is at 6 but s[6]=b is in dictionary at idx 1 outside our window
        elif (store[str[i]] < l):
            max_len = max(max_len, i-l+1)
        # case 3 - in the window so change l move to dictionary[i] + 1
        else:
            l = store[str[i]] + 1
        store[str[i]] = i


    return max_len



if __name__ == "__main__":
    str = "takeUforward"
    print("The length of the longest substring without repeating characters is", solve(str))
