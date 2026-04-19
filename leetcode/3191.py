class Solution(object):
    def minOperations(self, nums):
        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1
        
        res = 0
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] == 0:
                flip(nums, i)
                flip(nums, i + 1)
                flip(nums, i + 2)
                res += 1
        
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return res