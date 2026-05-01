from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # store indices
        result = []
        
        for i, num in enumerate(nums):
            # remove indices out of window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # remove smaller elements from back
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            dq.append(i)
            
            # window reached size k
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result