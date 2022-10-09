class Solution:
    def partition(self, s: str) -> List[List[str]]:
        global ans
        ans = []
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def helper(s, curr):
            global ans
            if len(s) == 0:
                ans.append(curr.copy())
            for i in range(len(s)):
                curr.append(s[:i+1])
                if isPalindrome(s[:i+1]):
                    helper(s[i+1:], curr)
                curr.pop()
        helper(s, [])
        return ans
            