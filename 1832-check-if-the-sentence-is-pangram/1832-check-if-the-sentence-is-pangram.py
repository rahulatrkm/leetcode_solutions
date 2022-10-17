class Solution:
    def checkIfPangram(self, s: str) -> bool:
        return len(set(list(s)))==26