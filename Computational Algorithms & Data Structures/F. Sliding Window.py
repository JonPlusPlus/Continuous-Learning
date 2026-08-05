# This demonstration utilises the Sliding Window technique
# to find the longest string of unique characters to a
# time complexity of O(n): Linear Time.
def lengthOfLongestSubstring(s):
    window = set()
    left = 0
    max_length = 0

    # Each character in the string is iterated through...
    for right in range(len(s)):
        # If we identify a character already in the set,
        # we remove the left-most value, so that there are
        # no duplicates in our mechanism counting for the
        # longest string of unique characters.
        # iteration-0, 'a' in set() == False
        # iteration-3, 'a' in set(a,b,c) == True
        while s[right] in window:
            window.remove(s[left])
            left += 1

        # We always add the newly read character to the set,
        # as we may have just deleted its duplicate, and we
        # still need to identify potential future duplicates.
        window.add(s[right])
        # This variable refreshes to be either the max-length
        # that we have found prior, or a newly found length
        # if it is longer.
        max_length = max(max_length, right - left + 1)

    # Once the loop has iterated over each character, it returns.
    return max_length

# Defines the string.
parentString = "abcabcdd"


# Calls, and prints, the function, inputting the string.
print(lengthOfLongestSubstring(parentString))
