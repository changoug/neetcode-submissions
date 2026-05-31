class Node:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        return self.search_node(self.root, 0, word)

    
    def search_node(self, node: Node, ind: int, word: str) -> bool:

        curr = node

        for i in range(ind, len(word)):
            print(word[i])
            if word[i] == '.':
                for c in curr.children:
                    if self.search_node(curr.children[c], i + 1, word):
                        return True
                return False

            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        
        return curr.word

        
