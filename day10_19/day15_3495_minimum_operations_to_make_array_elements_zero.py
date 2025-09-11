from typing import List
import math
MAX_VALUE = 1e9

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        beginArgumentOfLog = [0]
        quantityArgumentOfExponent = [0]
        tmp = 0
        exponent = 0

        while (tmp <= MAX_VALUE):
            beginArgumentOfLog.append(tmp)
            exponent += 1
            tmp = pow(4, exponent)
        beginArgumentOfLog.append(pow(4, exponent))
        beginArgumentOfLog[1] = 1

        lenBegin = len(beginArgumentOfLog)
        for i in range(1, lenBegin - 1):
            quantityArgumentOfExponent.append(beginArgumentOfLog[i + 1] - beginArgumentOfLog[i])
        
        m = len(queries)
        total = 0
        # print(beginArgumentOfLog)
        # print(quantityArgumentOfExponent)
        for i in range(m):
            firstIndex = int(math.log(queries[i][0], 4)) + 1
            lastIndex = int(math.log(queries[i][1], 4)) + 1
            arrayTmp = ([0] * firstIndex) + quantityArgumentOfExponent[firstIndex:lastIndex + 1]
            arrayTmp[firstIndex] = beginArgumentOfLog[firstIndex + 1] - queries[i][0]
            arrayTmp[lastIndex] = queries[i][1] - beginArgumentOfLog[lastIndex] + 1
            if (firstIndex == lastIndex):
                arrayTmp[lastIndex] = queries[i][1] - queries[i][0] + 1
            print(firstIndex, lastIndex, arrayTmp)

            for j in range(lastIndex, 0, -1):
                if (arrayTmp[j] == 0):
                    continue
                remainder = arrayTmp[j] % 2
                integer = arrayTmp[j] // 2

                if (j == 1):
                    total += integer + remainder
                    break

                total += integer * j
                if (remainder):
                    arrayTmp[1] += 1
                    arrayTmp[j - 1] += 1
        return total

S = Solution()
queries = [[5, 8]]
print(S.minOperations(queries))


