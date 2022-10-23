class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        d = set()
        xor = 0
        exp = 0
        for i,num in enumerate(nums):
            if num in d:
                ans[0] = num
            else:
                d.add(num)
                xor ^= num
            exp ^= (i+1)
        ans[1] = exp^xor
        return ans
        
            
        