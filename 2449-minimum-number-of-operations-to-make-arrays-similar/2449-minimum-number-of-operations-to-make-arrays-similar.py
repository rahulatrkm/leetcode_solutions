class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        on = sorted(num for num in nums if num%2)
        ot = sorted(num for num in target if num%2)
        en = sorted(num for num in nums if num%2 == 0)
        et = sorted(num for num in target if num%2 == 0)
        ans = 0
        ans += sum(abs(a-b)//2 for a,b in zip(on, ot))
        ans += sum(abs(a-b)//2 for a,b in zip(en, et))
        return ans//2