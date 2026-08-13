from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        pntr1 = 0
        pntr2 = len(nums)-1

        while pntr1 < pntr2:
            total = nums[pntr1] + nums[pntr2]

            if total == target:
                return [pntr1, pntr2]
            elif total < target:
                pntr1 += 1
            else:
                pntr2 -= 1
        return-1

init = Solution()
ans = init.twoSum([3,2,4],6)
print(ans)