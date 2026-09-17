class PrefixTree:

    def __init__(self):
        self.node = Trie()
        

    def insert(self, word: str) -> None:
        curr = self.node

        for c in word:
            i = ord(c) - ord('a')

            if not curr.letters[i]:
                curr.letters[i] = Trie()
            curr = curr.letters[i]
        
        curr.end = True


    def search(self, word: str) -> bool:

        curr = self.node

        for c in word:
            i = ord(c) - ord('a')

            if not curr.letters[i]:
                return False
            
            curr = curr.letters[i]

        if curr.end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.node

        for c in prefix:
            i = ord(c) - ord('a')
            if not curr.letters[i]:
                return False
            curr = curr.letters[i]

        return True
        
        

class Trie:

    def __init__(self):
        self.letters = [None] * 26
        self.end = False