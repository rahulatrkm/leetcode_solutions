class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        for i in range(1, n+1):
            curr = i
            while curr%5 == 0:
                curr //= 5
                cnt += 1
        return cnt