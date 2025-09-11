class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1_000_000_007
        progress = [[1, 1]] #item = [quantity, createAt]
        for day in range(2, n + 1):
            cnt = 0
            lenCur = len(progress)
            for j in range(lenCur):
                if (progress[j][1] + delay <= day) and (progress[j][1] + forget > day):
                    cnt = (cnt + progress[j][0]) % MOD
            progress.append([cnt, day])

        length = len(progress)
        result = 0
        for j in range(length):
            if progress[j][1] + forget > n:
                result = (result + progress[j][0]) % MOD
        result %= MOD
        return result
S = Solution()
n = 684
delay = 18
forget = 496
print(S.peopleAwareOfSecret(n, delay, forget))