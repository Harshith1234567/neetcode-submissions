class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pat=word[:j]+'*'+word[j+1:]
                nei[pat].append(word)

        q=deque([beginWord])
        visit=set()
        visit.add(beginWord)

        res=1
        while q:
            n=len(q)

            for i in range(n):
                word=q.popleft()
                if word==endWord:
                    return res

                for j in range(len(word)):
                    pat=word[:j]+'*'+word[j+1:]
                    for nw in nei[pat]:
                        if nw not in visit:
                            q.append(nw)
                            visit.add(nw)

            res+=1

        return 0
