class Node:

    def __init__(self):
        self.children = {}  # key will be character, value will be Node
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        current = self.root 
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
                current = current.children[char]
            else:
                current = current.children[char]
        current.isEnd = True 

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            else:
                current = current.children[char]        
        return current.isEnd 

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        return True 


# tc 
# insert - O(n) where n is length of a word 
# search - O(n) where n is length of a word. 
# startsWith - O(n) where n is length of a word 

# sc 
# insert - total nodes being created i.e. O(T) where T is unique characters is a given word
# search - O(1) no extra space
# startsWith - O(1) no extra space 