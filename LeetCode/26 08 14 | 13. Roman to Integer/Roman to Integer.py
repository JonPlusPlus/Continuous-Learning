# Achieves a linear time, O(n), and constant space, O(1), complexity.
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        for i in range(len(s)-1):
            # Numerals WITH a numeral larger than it directly to
            # its right have their value SUBTRACTED from the total.
            if numerals[s[i]] < numerals[s[i+1]]:
                total = total - numerals[s[i]]
            # Numerals WITHOUT a numeral larger than it directly to
            # its right have their value ADDED to the total.
            else:
                total = total + numerals[s[i]]
        # The last trailing numeral has nothing directly to its right,
        # so does not need evaluating, and can simply be added here.
        return(total + numerals[s[len(s)-1]])


# Dictionary holds the integer value for each numeral.
numerals = {
    'I':1, 'V':5, 'X':10, 'L':50,
    'C':100, 'D':500, 'M':1000
}

# Demo input.
num = 'MCMXCIV'

print(Solution().romanToInt(num))
