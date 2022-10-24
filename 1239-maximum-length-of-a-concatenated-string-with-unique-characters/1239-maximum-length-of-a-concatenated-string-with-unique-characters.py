class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def helper(idx, curr):
            if idx == len(arr):
                return len(curr)
            
            unq = set(list(arr[idx]))
            sidx = set()
            if len(unq) == len(arr[idx]):
                sidx = unq
            c1 = helper(idx+1, curr)
            c2 = 0
            if curr&sidx:
                c2 = helper(idx+1, sidx)
            else:
                c2 = helper(idx+1, curr|sidx)
            return max(c1, c2)
        
        
        return helper(0, set())
