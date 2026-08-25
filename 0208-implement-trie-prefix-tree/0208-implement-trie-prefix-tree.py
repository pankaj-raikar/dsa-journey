class Trie:

    def __init__(self):
        self.children= [None] * 26
        self.isWord=False
        

    def insert(self, word: str) -> None:
        node=self
        for c in word:
            index=ord(c)-ord("a")
            if node.children[index] is None:
                node.children[index]=Trie()
            node=node.children[index]

        node.isWord=True
        

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.isWord

        

    def startsWith(self, prefix: str) -> bool:
        node=self._traverse(prefix)
        return node is not None
    

    def _traverse(self,s:str):
        node=self

        for c in s:
            index=ord(c)-ord('a')
            if node.children[index] is None:
                return None
            node=node.children[index]

        return node


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)