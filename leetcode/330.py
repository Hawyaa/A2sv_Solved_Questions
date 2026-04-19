class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patches = 0
        miss = 1  
        i = 0
        length = len(nums)
        
        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]  
                i += 1
            else:
                miss += miss  
                patches += 1
        
        return patches