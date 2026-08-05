# Imports the 'heapq' module, to provide heap operations.
import heapq

# This demonstration uses the Heap technique to find the
# largest numbers from a list to a time complexity of
# O(nlogk): Linear Time × Logarithmic Operation.
def findKLargest(nums, k):
    heap = []

    # Each number is added to the heap, maintaining the
    # heap property.
    for num in nums:
        heapq.heappush(heap, num)

        # Once the size of the heap surpasses our
        # target-size, the smallest number is removed.
        if len(heap) > k:
            heapq.heappop(heap)

    # The final two values in the heap are returned.
    return heap


# Defines the list of integers.
nums = [3, 2, 1, 5, 6, 4]

# Calls, and prints, the function, specifying the inputs.
print(findKLargest(nums, 2))
