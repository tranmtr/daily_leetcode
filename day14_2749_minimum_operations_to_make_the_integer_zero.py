class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):
            num1 -= num2
            if (num1 > 0):
                if (num1.bit_count() <= i and i <= num1):
                    return i
            elif (num1 < 0):
                if (num2 >= 0):
                    return -1
                else:
                    continue
            else:
                return -1
        return -1