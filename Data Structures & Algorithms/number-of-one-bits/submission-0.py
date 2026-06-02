class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            print(bin(n))
            if n%2 == 1:
                count+=1
            n = n>>1
        return count
        