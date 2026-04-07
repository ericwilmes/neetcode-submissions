class TreeNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            c_pos = ord(c) - ord("a")
            c_node = curr_node.children[c_pos]
            if c_node is None:
                c_node = TreeNode()
                curr_node.children[c_pos] = c_node
            curr_node = c_node
        curr_node.end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            c_pos = ord(c) - ord("a")
            c_node = curr_node.children[c_pos]
            if c_node is None:
                return False
            curr_node = c_node
        return c_node.end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            c_pos = ord(c) - ord("a")
            c_node = curr_node.children[c_pos]
            if c_node is None:
                return False
            curr_node = c_node
        return True