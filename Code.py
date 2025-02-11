class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        t = ''
        for x in s:
            t += x
            if part in t:
                t = t[:t.index(part)]  
        return t
