class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramList = defaultdict(list)


        for string in strs:
            sortedChars = tuple(sorted(string))
            anagramList[sortedChars].append(string)
        
        anagrams = []
        for _,value in anagramList.items():
            anagrams.append(value)
        return anagrams
        