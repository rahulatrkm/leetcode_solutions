class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=0
        i = x
        if i <0:
            return False
        else:
            while i >0:
                a=i%10
                b=b*10 + a
                i=i//10
            # print(b, x)
            if b==x:
                return True
        return False