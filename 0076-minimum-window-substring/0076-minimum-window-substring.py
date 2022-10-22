class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
            
        def check(req={}, curr={}, char=None):
            for char in req:
                if char not in curr or req[char] > curr[char]:
                    return False
            
            return True
        
        req = {}
        for char in t:
            req[char] = req.get(char, 0) + 1
        
        j = 0
        n = len(s)
        m = (0,n-1)
        curr = {}
        isSol = False
        for i,char in enumerate(s):
            # print(curr, i)
            if char in req:
                curr[char] = curr.get(char, 0) + 1
            if check(req, curr, char):
                isSol = True
                # print(req, curr)
                while True:
                    # print(req, curr, "whi", j, i)
                    if s[j] in req and curr[s[j]] > req[s[j]]:
                        curr[s[j]] -= 1
                        j += 1
                    elif s[j] not in req:
                        j += 1
                    else:
                        break
                        
                if (m[1]-m[0]+1) > (i-j+1):
                    m = (j,i)                    
            
                
        if isSol:
            return s[m[0]:m[1]+1]
        return ""
                
                        