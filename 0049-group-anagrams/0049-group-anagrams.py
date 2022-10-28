class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_chars(word):
            return "".join(sorted(list(word)))
        
        d = {}
        for word in strs:
            k = sort_chars(word)
            if k in d:
                d[k].append(word)
            else:
                d[k] = [word]
        return d.values()