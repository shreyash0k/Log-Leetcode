class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        result = 1 
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(0,len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        queue = deque()
        queue.append(beginWord)
        visited = set([beginWord])
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for i in range(0,len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in adj[pattern]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            result = result + 1 
        
        return 0 

