class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if not curr.children[pos]:
                curr.children[pos] = Node()
            curr = curr.children[pos]
        curr.end = True
        


    def search(self, word: str) -> bool:
        def sub(i: int, root) -> bool:
            if i == len(word):
                return root and root.end
            if not root:
                return False

            c = word[i]
            if c == '.':
                for node in root.children:
                    if node and sub(i + 1, node):
                        return True
                return False
            pos = ord(c) - ord('a')
            child = root.children[pos]
            if child:                     
                return sub(i + 1, child)
            return False                  

        return sub(0, self.root)
