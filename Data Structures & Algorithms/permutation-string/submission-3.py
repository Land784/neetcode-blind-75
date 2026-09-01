from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1counts = Counter(s1)
        
        i,j = 0,len(s1)-1

        for _ in range(0, len(s2)-len(s1)+1):
            s2Counter = Counter(s2[i:j+1])
            if s1counts == s2Counter:
                return True
            else:
                i += 1
                j += 1
        return False
                