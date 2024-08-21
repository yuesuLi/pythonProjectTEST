class Solution:

    def __init__(self):
        self.count = 0

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        visited = set()
        visited.add(beginWord)
        ordA = ord('a')
        from collections import deque
        q = deque([beginWord])
        mapping = {beginWord: 1}
        while q:
            word = q.popleft()
            path = mapping[word]

            for i in range(n):
                word_List = list(word)
                for j in range(26):
                    tmpChar = chr(ordA + j)
                    word_List[i] = tmpChar
                    tmpS = ''.join(word_List)
                    if tmpS == endWord:
                        return path + 1
                    if tmpS in wordList and tmpS not in visited:
                        q.append(tmpS)
                        mapping[tmpS] = path + 1
                        visited.add(tmpS)
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
sol = Solution()
ret = sol.ladderLength(beginWord, endWord, wordList)
print(ret)

print()
