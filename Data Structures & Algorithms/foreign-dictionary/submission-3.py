class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def compare(word1, word2):
            minlen = min(len(word1), len(word2))
            for i in range(minlen):
                if word1[i] != word2[i]:
                    return (word1[i], word2[i])
            if len(word2) >= len(word1): return ('.', '.')  # Can't get edge but it's valid
            return ('/', '/')    # Invalid pair, just return

        # Step 1, build graph
        mp, adj = {}, {} # In-degree map and adjacency list
        # Build all the letters first and initialize in-degree
        for word in words:
            for letter in word:
                if letter not in mp: mp[letter] = 0

        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            a, b = compare(word1, word2)        # Two letters with an edge
            if a == '/': return ""
            if a == '.': continue
            if b not in adj.get(a, set()):
                if a not in adj: adj[a] = set()
                adj[a].add(b)
                mp[b] += 1

        q = []      # Queue for pool of roots
        # Step 2, reconstruct path
        for l, d in mp.items():     # letter, incoming degree
            if d == 0: q.append(l)

        size = len(mp)
        result = ""
        while q:
            letter = q.pop(0)
            result += letter
            if letter in adj:
                for neighbor in adj[letter]:
                    mp[neighbor] -= 1
                    if mp[neighbor] == 0:
                        q.append(neighbor)
        if len(result) == size: return result
        return ""
            


            

    
    