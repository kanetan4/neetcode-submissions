from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            key = [0] * 26

            for char in string:
                index = ord(char) - ord('a')
                key[index] += 1
            
            hashmap[tuple(key)].append(string)

        result = [x for x in hashmap.values()]

        return result