# A brute-force approach, iterating through to check every pairing combination would take O(n^2) time.
# Instead, a Hash Map approach achieves O(n) time and O(n) space while preserving original indices.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("unsorted:\t",nums)
        # Sort list for 'Two-Pointers' algorithm:
        # HYPOTHETICALLY: incrementing to compare every element with every other element in an unsorted list = O(n^2)
        # HERE: the 'sort' with the addition of running Two Pointers on a now-sorted list overall = O(n log n)
        # NOTE: the now-sorted Two Pointer traversal itself = O(n)
        nums.sort()

        pntr1 = 0
        pntr2 = len(nums)-1

        # Iterates until such a time that the pointers are equal, in which case, the code returns an empty list, as expected in the class's annotations.
        while pntr1 < pntr2:
            # Compare the current pair's sum with the target.
            total = nums[pntr1] + nums[pntr2]

            # Upon an iteration where we have found the sum of our target, we return those indices from the sorted list.
            # Outside this class, we then equate the 'sorted' indices with their original position via a Hash Map.
            if total == target:
                return [pntr1, pntr2]
            # When the sum is too small, we shift the left-pointer rightwards to increase the sum.
            elif total < target:
                pntr1 += 1
            # When the sum is too big, we shift the right-pointer leftwards to decrease the sum.
            else:
                pntr2 -= 1
        return []

# Define demo inputs.
nums = [3,2,4]
target = 6

# Populating Hash Map, to remember the original placements in the array.
hashmap = {}
for n in range(len(nums)):
    hashmap[nums[n]] = n

# Initialises the class, as we do not directly call a constructor due to the lack of the __init__ method.
init = Solution()
ans = init.twoSum(nums,target)
# Use the returned values to look up their original indices in the Hash Map.
print("sorted:\t\t",nums)
print("dict:\t\t",hashmap)
print("output:\t\t",ans[0],ans[1])
print("nums:\t\t",nums[ans[0]],nums[ans[1]])
print(hashmap.get(ans[0]),hashmap.get(ans[1]))
print(hashmap[nums[ans[0]]],hashmap[nums[ans[1]]])
