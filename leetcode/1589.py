class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        MOD = 10**9 + 7
        n = len(nums)
        diff = [0] * (n + 1)
        
        for start, end in requests:
            diff[start] += 1
            diff[end + 1] -= 1
        
        freq = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            freq[i] = curr
        
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        total = 0
        for i in range(n):
            total = (total + freq[i] * nums[i]) % MOD
        
        return total