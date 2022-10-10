class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        for i,char in enumerate(palindrome):
            if char != "a":
                if len(palindrome)%2 == 0:
                    return palindrome[:i] + "a" + palindrome[i+1:]
                elif i != len(palindrome)//2:
                    return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"
                    
                