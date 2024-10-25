import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        
        # Build a min-heap of size k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
         if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
         elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        
        # The root of the heap is the k-th largest element
         return self.min_heap[0]

# Example usage
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10)) # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8
        


