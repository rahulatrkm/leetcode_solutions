class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set(list(sentence))
        if len(sentence) == 26:
            return True
        return False