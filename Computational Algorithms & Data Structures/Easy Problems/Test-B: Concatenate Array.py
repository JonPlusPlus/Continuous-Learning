########################################
# PROMPT
########################################
# Given [1,2,1], return [1,2,1,1,2,1].
########################################

# Initialises a function to concatenate two lists.
def concatenate(nums):
    # Concatenates both lists, and returns the result.
    nums = nums + nums
    return nums


# Defines the pre-set list.
nums = [1,2,1]

# Calls, and prints, the function's output.
print(concatenate(nums))