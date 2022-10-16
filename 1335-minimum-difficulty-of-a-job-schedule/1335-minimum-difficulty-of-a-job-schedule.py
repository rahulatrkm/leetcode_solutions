class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def helper(jobs, d):
            # print(jobs, d)
            if len(jobs) < d:
                return float('inf')
            if len(jobs) == d:
                return sum(jobs)
            if d == 1:
                return max(jobs)
            if d <= 0:
                return float('inf')
            curr = jobs[0]
            ans = float('inf')
            for i in range(len(jobs)-d+1):
                curr = max(curr, jobs[i])
                # print(helper(jobs[i+1:], d-1))
                ans = min(ans, curr+helper(jobs[i+1:], d-1))
                # print("curr", curr)
            # print(ans)
            return ans
        val = helper(tuple(jobDifficulty), d)
        if val == float('inf'):
            return -1
        return val