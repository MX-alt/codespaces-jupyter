class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        
        if len1 > len2:
            return self.oneEditAway(second, first)

        if len2 - len1 > 1:
            return False

        for i in range(len1):
            if first[i] != second[i]:
                if len1 == len2:
                    return first[i+1:] == second[i+1:]
                else:
                    return first[i:] == second[i+1:]

        return len(second) - len(first) <= 1