class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        ans = []
        curr = prev[0]
        cnt = 0
        for char in prev:
            if char == curr:
                cnt += 1
            else:
                ans.append(str(cnt))
                ans.append(curr)
                curr = char
                cnt = 1
        ans.append(str(cnt))
        ans.append(curr)
        return "".join(ans)
                