class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0 
        best = 0
        counts = {}

        for r, char in enumerate(s):
            counts[char] = counts.get(char,0) + 1

            while sum(counts.values()) - max(counts.values()) > k:
                print("hit")
                counts[s[l]] -= 1
                l += 1
            best = max(best,r-l + 1)
            print(best)
        
        return best

 
