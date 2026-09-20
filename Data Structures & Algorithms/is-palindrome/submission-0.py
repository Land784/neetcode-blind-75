class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        print(newString)
        left, right = 0, len(newString)-1
        while left < right:
            if newString[left] != newString[right]:
                return False
            left += 1
            right -= 1
        
        return True
        