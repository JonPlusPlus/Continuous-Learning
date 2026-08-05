########################################
# PROMPT
########################################
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
########################################

# Initialises a Two-Pointers function to solve
# the Two Sum problem of finding two numbers in
# a list that add together to make a target number.
# Time-Complexity: O(n)
def twoPointers(nums, target):
    left = 0
    right = len(nums) -1
    nums.sort()

    # Numbers are added together until the target is found.
    for num in nums:
        # Once the pair is found, they are returned.
        if nums[left] + nums[right] == target:
            return (left, right)

        # If the attempted pair is too small, the left pointer
        # increments to try a higher number.
        elif nums[left] + nums[right] < target:
            left += 1

        # If the attempted pair is too high, the right pointer
        # decrements to try a lower number.
        else:
            right -= 1

    # If no solution is found, we return an error.
    return -1

# Declares list of integers, and our target number.
nums = [2,7,11,15]
target = 9

# Calls, and prints, the function.
print(twoPointers(nums,target))