class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        curpos = text.split(" ")
        cnt = 0
        for x in curpos:
            if (set(x) & broken_set):
                continue
            cnt += 1
        return cnt

S = Solution()
text = "hello world"
brokenLetters = "ad"
print(S.canBeTypedWords(text, brokenLetters))