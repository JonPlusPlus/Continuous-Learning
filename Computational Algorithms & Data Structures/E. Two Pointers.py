# This example will demonstrate using the Two Pointers
# principles to identify two numbers that are the sum of a
# target value, to a time complexity of O(n): Linear time.
def two_sum_sorted(nums,target):

    # Define two variables, 'left' as 0, and 'right' as
    # whatever the length of the 'nums' list is, minus 1.
    left = 0
    right = len(nums)-1

    # Initialises a loop while the 'left' variable is less
    # than 'right', so as to exit if the two pointers meet.
    while left < right:

        # Initialises a variable equal to the sum of the
        # two values in 'nums' that the 'left' and 'right'
        # variables points to.
        total = nums[left]+nums[right]

        # If 'total' is of equal value to 'target', we have
        # found our sum, and the function returns.
        if total == target:
            return [left,right]

        # If 'total' is lower than 'target', then the 'left'
        # pointer is incremented rightwards one.
        elif total < target:
            left += 1

        # If 'total' is higher than 'target', then the
        # 'right' pointer is incremented leftwards one.
        else:
            right -= 1

    # Returns None if no pair exists that sums to the target.
    return None


# Calls the function, specifying the input list and target,
# and prints the returned output.
print(two_sum_sorted([1,2,4,6,8],10))
