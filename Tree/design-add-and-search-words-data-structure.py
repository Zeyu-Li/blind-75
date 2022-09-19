class Node:
    def __init__(self):
        self.children = dict()
        self.end = False


class WordDictionary:
    # use Trie
    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.end = True # sets last as end
        

    def search(self, word: str) -> bool:
        # def dfs(index: int, root: Node) -> bool:
        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # for all possible combinations
                    for child in curr.children.values():
                        if dfs(i+1, child): return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)