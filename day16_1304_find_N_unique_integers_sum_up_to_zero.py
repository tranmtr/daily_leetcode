from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        start = -(n // 2)
        end = n // 2
        for i in range(start, end + 1):
            result.append(i)
        if (n % 2 == 0):
            result.remove(0)
        return result
        