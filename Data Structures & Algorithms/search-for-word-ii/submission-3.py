class Node:
    def __init__(self):
        self.passes = 0
        self.end = 0
        self.next: list[Node | None]= [None for i in range(26)]


class Solution:
    def build(self, words: list[str]):
        for word in words:
            node = self.root
            for c in word:
                index = ord(c) - ord('a')
                if not node.next[index]: node.next[index] = Node()
                node = node.next[index]
                node.passes += 1
            node.end += 1

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Node()
        self.build(words)
        result = []

        def recur(pos, visited: dict, node: Node, word: str) -> int:
            words_found = 0
            if node.end > 0:
                result.append(word)
                node.end = 0
                words_found += 1

            x, y = pos
            for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (next_x, next_y) not in visited and 0 <= next_x < len(board[0]) and 0 <= next_y < len(board):
                    ch = board[next_y][next_x]
                    idx = ord(ch) - ord('a')
                    next_node = node.next[idx]
                    if not next_node or next_node.passes == 0:
                        continue
                    visited[(next_x, next_y)] = 1
                    words_found += recur((next_x, next_y), visited, next_node, word + ch)
                    visited.pop((next_x, next_y))
            node.passes -= words_found
            return words_found


        for i in range(len(board)):
            for j in range(len(board[0])):
                index = ord(board[i][j]) - ord('a')
                if not self.root.next[index]: continue
                node = self.root.next[index]
                recur((j, i), {(j, i): 1}, node, board[i][j])

        return result
                
                

                            
