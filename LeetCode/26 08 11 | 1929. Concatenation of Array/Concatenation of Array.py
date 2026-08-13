# Time complexity is O(n), because we copy 2n elements, and 2 is a constant.
# Space complexity is O(n), because the returned list contains 2n elements.
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Creates a new list and the local variable is then rebound to it.
        return nums + nums


# Initialises demo input.
# We do not directly call a constructor because there is no __init__ method
init = Solution()
ans = init.getConcatenation([1, 3, 2, 1])
# Prints the return output of the function, when the demo input is used.
print(ans)
