class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = -1
        for num in nums:
            if -num in nums:
                ans = max(ans, num)
        return ans