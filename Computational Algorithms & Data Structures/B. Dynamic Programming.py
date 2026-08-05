# This Dynamic Programming (DP) example will uses
# Tabulation to calculate a target number in the Fibonacci
# sequence to a time complexity of O(n): Linear Time.
def fibonacci(n):

    # Initialises a list, and generates a number of positions
    # to that of the input (in this case 10) plus 1.
    dp = [0] * (n+1)

    # Pre-populates the first two zero-indexed positions in
    # the list as 0 and 1 respectively.
    dp[0] = 0
    dp[1] = 1


    # Each new value of index 2 onward is calculated via the
    # sum of the prior two entries (i-1 and i-2).
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    # Once calculated via the iterative loop, we can
    # return the value at the specified index (10), which
    # in this case, is 55.
    result = print("value", dp[n], "was at position", n)
    return result


# Calls the function, specifying a target index.
fibonacci(10)
