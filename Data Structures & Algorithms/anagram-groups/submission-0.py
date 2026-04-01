class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        d = {}
        for i, word in enumerate(strs):
            hash = [0] * 26
            for c in word:
                hash[ord(c) - ord('a')] += 1
            if tuple(hash) in d:
                d[tuple(hash)].append(word)
            else:
                d[tuple(hash)] = [word]
        return list(d.values())
        