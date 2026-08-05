# This Binary Search algorithm will iteratively search
# an ordered list to find a specified value to a
# maximum time-complexity of O(log n): Logarithmic Time.
def binary_search(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        # Finds the middle index using floor-division:
        # e.g. ⌊(0+5)÷2⌋=2
        mid = (left + right)//2

        # Returns the 'target' when found.
        if nums[mid] == target:
            result = print("value",
                         nums[mid],
                         "was at position",
                         mid)
            return result

        # Moves to check the right-hand side of the list
        # if the checked value is smaller than the 'target'.
        elif nums[mid] < target:
            left = mid + 1

        # Moves to check the left-hand side of the list
        # if the checked value is bigger than the 'target'.
        else:
            right = mid - 1

    # Returns a sentinel-value if the conditions are not met.
    return -1


# Initialises the list.
nums = [1,3,5,7,9,11]

# Calls the function, specifying a 'target' value.
binary_search(nums, 7)
