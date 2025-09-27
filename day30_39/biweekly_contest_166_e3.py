class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        result = set()
        cnt_U, cnt_D, cnt_L, cnt_R = 0, 0, 0, 0
        for j in range(k):
            if (s[j] == 'U'):
                cnt_U += 1
            elif (s[j] == 'D'):
                cnt_D += 1
            elif (s[j] == 'L'):
                cnt_L += 1
            elif (s[j] == 'R'):
                cnt_R += 1
        p = (cnt_U - cnt_D, cnt_L - cnt_R)
        result.add(p)      
        
        for j in range(k, n):
            if (s[j] == 'U'):
                cnt_U += 1
            elif (s[j] == 'D'):
                cnt_D += 1
            elif (s[j] == 'L'):
                cnt_L += 1
            elif (s[j] == 'R'):
                cnt_R += 1

            if (s[j - k] == 'U'):
                cnt_U -= 1
            elif (s[j - k] == 'D'):
                cnt_D -= 1
            elif (s[j - k] == 'L'):
                cnt_L -= 1
            elif (s[j - k] == 'R'):
                cnt_R -= 1

            p = (cnt_U - cnt_D, cnt_L - cnt_R)
            result.add(p)
        return len(result)