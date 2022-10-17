class Solution:
    def checkIfPangram(self, s: str) -> bool:
        return len(Counter(s))==26