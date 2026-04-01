class Node:
    def __init__(self):
        self.passes = 0
        self.end = 0
        self.next: list[Node | None] = [None for i in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        node.passes += 1
        for c in word:
            index = ord(c) - ord('a')
            if not node.next[index]:
                node.next[index] = Node()
            node = node.next[index]
            node.passes += 1
        node.end += 1

    def search(self, word: str):
        return self.recur(self.root, word, 0)

    def recur(self, node: Node, word: str, i: int) -> bool:
        if i >= len(word):
            if node.end: return True
            else: return False
        c = word[i]
        if c == '.':
            for j in range(26):
                if node.next[j]:
                    if self.recur(node.next[j], word, i+1): return True
            return False
        else:
            index = ord(c) - ord('a')
            if not node.next[index]:
                return False
            return self.recur(node.next[index], word, i + 1)
        
