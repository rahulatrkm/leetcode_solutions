class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = j = 0
        jmin = jmax = -1
        for i,a in enumerate(nums):
            if not minK <= a <= maxK:
                jmin, jmax, j = -1, -1, i + 1
            if a == minK: jmin = i
            if a == maxK: jmax = i
            res += max(0, min(jmin, jmax) - j + 1)
        return res