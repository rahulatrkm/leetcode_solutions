class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def calc_hash(word, l):
            curr = ["26"]*l
            # print(curr)
            for i,char in enumerate(word):
                curr[i] = str(ord('z')-ord(char))
                if len(curr[i]) == 1:
                    curr[i] = "0" + curr[i]
            return "".join(curr)
        
        freq = collections.defaultdict(int)
        l = 0
        for word in words:
            freq[word] += 1
            l = max(len(word), l)
        
        topk = []
        for word in freq:
            hsh = calc_hash(word, l)
            if len(topk) < k:
                heapq.heappush(topk, (freq[word], hsh, word))
            else:
                if (topk[0][0], topk[0][1]) < (freq[word], hsh):
                    heapq.heappop(topk)
                    heapq.heappush(topk, (freq[word],hsh, word))
                
            # print(topk)
        ans = []
        topk.sort(key = lambda x: (-x[0], x[2]))
        for word in topk:
            ans.append(word[2])
        return ans
            