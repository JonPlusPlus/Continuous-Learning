# Put simply, the solution achieves linear complexity in both time and space: O(n).
# More accurately, O(d) is achieved, where d = the number of digits in x.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Initialise an array called modulus (mod).
        # 121 mod 10 = 1, 12 mod 10 = 2, 1 mod 10 = 1 | mod[1,2,1]
        mod = []

        if x >= 0:
            while x > 0:
                # Appends the last digit of an integer to the list.
                # Maintaining the original order is not necessary, as we are looking
                # for palindromes, which are the same when mirrored | 121==121, 10!=01
                mod.append(x % 10)
                x = x // 10

            for m in range(len(mod)//2):
                # Check each element matches its mirrored position.
                # mod[0]==mod[-1], mod[1]==mod[-2], mod[2]==mod[-3], etc...
                if mod[m] == mod[(len(mod) - 1) - m]:
                    continue
                else:
                    return False

            return True

        else:
            return False


init = Solution()
ans = init.isPalindrome(121)

# Will output True for any palindrome.
# Negative numbers are not considered palindromes due to the leading minus symbol.
# In=121|Out=True, In=-121|Out=False, In=10|Out=False
print(ans)