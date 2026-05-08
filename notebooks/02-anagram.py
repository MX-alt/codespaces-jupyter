class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        counts = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            counts[index] += 1

        for char in s2:
            index = ord(char) - ord('a')
            counts[index] -= 1

        if any(counts):
            return False
        
        return True