class Trie:
    def __init__(self):
        self.dic={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=Trie()



    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.dic:
                cur.dic[c]=Trie()
            cur=cur.dic[c]
        cur.end=True

        

    def search(self, word: str) -> bool:
        def dfs(cur,idx):
            
                
            c=word[idx]

            if idx==len(word)-1:
                if c=='.' :
                    for e in cur.dic:
                        if cur.dic[e].end:
                            return True
                    return False
                elif c in cur.dic:
                    return cur.dic[c].end
                else:
                    return False

            if c=='.':
                for e in cur.dic:
                    if dfs(cur.dic[e],idx+1):
                        return True
                return False

            elif c in cur.dic :
                return dfs(cur.dic[c],idx+1)

            return False
        
        return dfs(self.root, 0)
        
