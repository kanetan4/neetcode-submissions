class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {} # key is a tuple (cars, car) of string, word in dict, and key will be s
        length = [len(word) for word in wordDict]

        
        def recursion(string: str):
            for i, word in enumerate(wordDict):
                if string == "":
                    return True
                if string[0:length[i]] == word:
                    if (string, word) in cache: continue
                    if recursion(string[length[i]:]): return True
                    else: 
                        cache[(string, word)] = False
                        continue
            return False

        return recursion(s)
