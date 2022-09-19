class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.refs = 0

    def addWord(self, word):
        curr = self
        curr.refs += 1
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.refs += 1
        curr.end = True

    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
                curr.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                node.end = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
    
# brute force
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         rows, cols = len(board), len(board[0])
        
#         visited = set()
        
#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
#             if (0 > r or 0 > c or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in visited):
#                 return False
        
#             visited.add((r,c))
            
#             res = (dfs(r+1, c, i+1) or
#                    dfs(r-1, c, i+1) or
#                    dfs(r, c+1, i+1) or
#                    dfs(r, c-1, i+1))
            
#             visited.remove((r,c))
            
#             return res
            
#         for r in range(rows):
#             for c in range(cols):
#                 if dfs(r,c,0): return True
#         return False
    
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         res = []
#         for word in words:
#             if self.exist(board, word):
#                 res.append(word)
            
#         return res