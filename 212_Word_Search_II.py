class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        current = self 
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        
        current.isWord = True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        rows = len(board)
        cols = len(board[0])
        for w in words:
            root.addWord(w)
        
        result = set()
        directions= [(0,1),(0,-1),(-1,0),(1,0)]
        visited = set()

        def dfs(row,col,current,string):
            if board[row][col] not in current.children:
                return
            current = current.children[board[row][col]]
            if current.isWord:
                result.add(string)
            
            visited.add((row,col))
            for dr, dc in directions:
                new_row = dr+row
                new_col = dc+col
                if (0<=new_row<rows and 0<=new_col<cols and (new_row,new_col) not in visited):
                    dfs(new_row,new_col,current, string+ board[new_row][new_col])
            
            visited.remove((row,col))
            

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,board[i][j])
        
        return list(result)        