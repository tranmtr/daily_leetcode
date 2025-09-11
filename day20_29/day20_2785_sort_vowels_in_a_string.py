class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        vowels = set("aeiouAEIOU")
        for x in s:
            if(x in vowels):
                res.append(x)
        res.sort()
        cnt = 0
        lst = []
        for x in s:
            if (x in vowels):
                lst.append(res[cnt])
                cnt += 1
            else:
                lst.append(x)
        return "".join(lst)

a = "lEetcOde"
S = Solution()
print(S.sortVowels(a))