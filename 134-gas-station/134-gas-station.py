class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = 0
        prev = 0
        ans = 0
        for i in range(len(gas)):
            curr = gas[i]-cost[i]
            if prev+curr < 0:
                prev = 0
                ans = i+1
            else:
                prev += curr
            tot += curr
        if tot < 0:
            return -1
        return ans
                