class Solution:
    def __init__(self):
        self.children=[None] * 26
        self.isEnd=False
    
    def insert(self,word:str)->None:
        node=self

        for c in word:
            index=ord(c)-ord("a")
            if node.children[index] is None:
                node.children[index]=Solution()
            
            node=node.children[index]
        node.isEnd=True 

    def search(self,word:str):
        node=self._traverse(word)  
        return node 
    
    def _traverse(self,word:str):
        node=self

        for i,c in enumerate(word):
            index=ord(c)-ord("a")

            if node.children[index] is None:
                return ""
            
            node=node.children[index]

            if node.isEnd:
                return word[:i+1]
            
        return ""
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        for word in dictionary:
            self.insert(word)

        splitSentence=sentence.split()

        output=""
        for c in splitSentence:
            serch=self.search(c)
            print(serch)
            if serch:
                output+=serch + " "
            else:
                output+=c + " "

        return output.strip()

        
        