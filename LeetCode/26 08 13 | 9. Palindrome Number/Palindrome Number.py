# Achieves logarithmic time, O(log₁₀n), where n is the value of x,
# and constant space, O(1), complexity, using only constant auxiliary space.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Any negative number, or number ending in zero, other than zero itself, returns False.
        # Not catching numbers that end in zero causes the logic below to break, as integers can't have leading zeros.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Variable becomes mirror of the latter-half of x, for comparison with the first.
        half_mirror = 0

        while x > half_mirror:
            # Extract last digit of x, and append into last digit of half_mirror:
            # x=121,hm=0 -> x=12,hm=1 -> x=1,hm=12
            half_mirror = half_mirror * 10 + x % 10
            x //= 10

        return x == half_mirror or x == half_mirror // 10


init = Solution()
ans = init.isPalindrome(121)

# Will output True for any palindrome.
# Negative numbers are not considered palindromes due to the leading minus symbol.
# In=121|Out=True, In=-121|Out=False, In=10|Out=False
print(ans)