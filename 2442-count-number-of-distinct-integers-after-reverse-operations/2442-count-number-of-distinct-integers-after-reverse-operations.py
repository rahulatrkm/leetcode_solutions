class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)
        for num in nums:
            ans.add(int(str(num)[::-1]))
        return len(ans)