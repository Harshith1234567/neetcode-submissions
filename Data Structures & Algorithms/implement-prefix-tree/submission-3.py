class Node:
    def __init__(self):
        self.dic={}
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        node=self.root

        for w in word:
            if w not in node.dic:
                node.dic[w]=Node()
            node=node.dic[w]
        node.end=True

    def search(self, word: str) -> bool:
        node=self.root

        for w in word:
            if w not in node.dic:
                return False
            node=node.dic[w]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node=self.root

        for w in prefix:
            if w not in node.dic:
                return False
            node=node.dic[w]
        return True
        