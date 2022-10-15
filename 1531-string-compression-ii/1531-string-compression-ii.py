class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def counter(start, last, last_count, k):
            if k < 0: return float('inf')
            if start == len(s): return 0
            if s[start] == last:
                delta = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                return delta + counter(start+1, last, last_count+1, k)
            else:
                keep_cnt = 1 + counter(start+1, s[start], 1, k)
                delete_cnt = counter(start+1, last, last_count, k - 1)
                return min(keep_cnt, delete_cnt)
        return counter(0,"",0,k)