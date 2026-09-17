class WordDictionary:

    def __init__(self):
        self.root = Trie()

        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.letters:
                node.letters[c] = Trie()
            node = node.letters[c]
        
        node.end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(j, node):
            n = node
            for i in range(j, len(word)):
                if word[i] == '.':
                    for letter in n.letters.values():
                        if dfs(i + 1, letter):
                            return True
                    return False
                else:
                    if word[i] not in n.letters:
                        return False
                    n = n.letters[word[i]]
            return n.end

        return dfs(0, self.root)



class Trie:

    def __init__(self):
        self.letters = {}
        self.end = False