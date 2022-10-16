class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        for i in range(num):
            a=str(i)[::-1]
            if i+int(a)==num:
                return True
        return False