class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        idx,m = 0,float('inf')
        rsum = 0
        for i,num in enumerate(nums):
            rsum += num
            left = (rsum//(i+1))
            right = 0
            if (n-i-1) != 0:
                right = (s-rsum)//(n-i-1)
            curr = abs(left - right)
            if curr < m:
                m,idx = curr,i
        return idx