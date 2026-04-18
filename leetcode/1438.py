from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_len = 0
        
        for right, num in enumerate(nums):
            # Maintain max_deque (decreasing order)
            while max_deque and nums[max_deque[-1]] <= num:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min_deque (increasing order)
            while min_deque and nums[min_deque[-1]] >= num:
                min_deque.pop()
            min_deque.append(right)
            
            # Shrink window if condition violated
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update maximum length
            max_len = max(max_len, right - left + 1)
        
        return max_len