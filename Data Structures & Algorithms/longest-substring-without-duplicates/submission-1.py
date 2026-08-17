class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        present = {}
        maxWindow = 1
        l = 0        
        for r, char in enumerate(s):
            if char in present and present[char] >= l:
                l = present[char] + 1
            
            present[char] = r

            maxWindow = max(maxWindow,r-l+1)
        return maxWindow
            


