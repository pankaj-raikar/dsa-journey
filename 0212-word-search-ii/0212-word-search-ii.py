class Solution:
    def __init__(self):
        self.children=[None] * 26
        self.isEnd=False
        self.word=""
    
    
    def insert(self,word:str)->None:
        node=self

        for c in word:
            index=ord(c)-ord("a")
            if node.children[index] is None:
                node.children[index]=Solution()
            
            node=node.children[index]
        node.isEnd=True 
        node.word=word

    def search(self,word:str):
        node=self._traverse(word)  
        return node 
    
    def _traverse(self,board,i,j,node):

        if (i<0 or i >= self.m or j>=self.n or j<0 ):
            return 
        
        if board[i][j] == "$" or node.children[ord(board[i][j])-ord("a")] is None:
            return

        node = node.children[ord(board[i][j])-ord("a")]

        if (node.isEnd):
            self.result.append(node.word)
            node.isEnd = False
        
        temp = board[i][j]

        board[i][j]="$"

        for dir in self.direction:
            new_i=i+dir[0]
            new_j=j+dir[1]

            self._traverse(board,new_i,new_j,node)

        board[i][j]=temp
            
        return ""
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.m=len(board)
        self.n=len(board[0])
        self.result=[]
        self.direction= [[1,0],[-1,0],[0,1],[0,-1]]
        node = self
        for w in words:
            self.insert(w)
        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                index=ord(c)-ord("a")
                if node.children[index] is not None:
                    self._traverse(board,i,j,node)

        return self.result

        
        