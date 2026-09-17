class PrefixTree:

    def __init__(self):
        self.node = Trie()
        

    def insert(self, word: str) -> None:
        curr = self.node

        for c in word:

            if c not in curr.letters:
                curr.letters[c] = Trie()
            curr = curr.letters[c]
        
        curr.end = True


    def search(self, word: str) -> bool:

        curr = self.node

        for c in word:

            if c not in curr.letters:
                return False
            
            curr = curr.letters[c]

        if curr.end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.node

        for c in prefix:
            if c not in curr.letters:
                return False
            curr = curr.letters[c]

        return True
        
        

class Trie:

    def __init__(self):
        self.letters = {}
        self.end = False