class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, depth = queue.popleft()
            if word == endWord: return depth
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in wordList and newWord not in visited:
                        queue.append((newWord, depth + 1))
                        visited.add(newWord)
        return 0
        



        
            
        