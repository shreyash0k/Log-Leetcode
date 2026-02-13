class Trie:
    def __init__(self):
        self.children = {} # "a":{}, "b":{}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.isWord = True

    
    def search(self, word: str) -> bool: #.pple   [apple, alan, ada, apar]  {d}, {l}, {p}, 
        
        def dfs(index, node):
            current = node
            for i in range(index,len(word)):
                if word[i] == ".":
                    for node in current.children.values():
                        if dfs(i+1,node):
                            return True
                    return False
                if word[i] not in current.children:
                    return False
                current = current.children[word[i]]
            return current.isWord    
            
        return dfs(0,self.root)

        

# tc for search O(26^L) where L is length of searched word 