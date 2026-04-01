class Node:
    def __init__(self):
        self.passes = 0
        self.end = 0
        self.next: list[Node | None] = [None for i in range(26)]

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        node.passes += 1
        for c in word:
            index = ord(c) - ord('a')
            if not node.next[index]:
                node.next[index] = Node()
            node = node.next[index]
            node.passes += 1
        node.end += 1

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.next[index]:
                return False
            node = node.next[index]
        if node.end: return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not node.next[index]:
                return False
            node = node.next[index]
        return True
        
        