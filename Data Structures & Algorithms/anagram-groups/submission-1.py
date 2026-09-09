class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = []
        
        wordMap = {}
        index = 0
        for word in strs:
            letterCount = {}
            counts = [0] * 26
            for i in range(len(word)):
                counts[ord(word[i]) - ord('a')] += 1
            key = tuple(counts)
            if key in wordMap:
                anagramList[wordMap[key]].append(word)
            else:
                wordMap[key] = index
                anagramList.append([word])
                index += 1
        return anagramList