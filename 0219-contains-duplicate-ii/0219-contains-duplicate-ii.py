class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(min(k+1, len(nums))):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        
        i = k+1
        j = 0
        while i < len(nums):
            s.remove(nums[j])
            if nums[i] in s:
                return True
            s.add(nums[i])
            i += 1
            j += 1    
        return False
                