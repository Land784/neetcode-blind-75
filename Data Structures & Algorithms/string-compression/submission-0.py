class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0
        s = []
        if len(chars) == 1:
            #s = chars[0]
            return 1

        prev = None
        for index, char in enumerate(chars):
            count = 1
            for i in range(index+1,len(chars)):
                if chars[i] == char:
                    count += 1
                else:
                    break
            if prev != char:

                s.append(char)
                if count == 1:
                    k += 1
                else:
                    s.extend([*str(count)])
                    k += 1 + len(str(count))
            prev = char

        chars[:k] = s
        return k

            






