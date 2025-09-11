from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        m = len(classes)
        max_heap = []
        for i in range(m):
            tmp = (classes[i][0] + 1) / (classes[i][1] + 1) - (classes[i][0] / classes[i][1])
            item = (-tmp, i)
            heapq.heappush(max_heap, item)

        for _ in range(extraStudents):
            item = heapq.heappop(max_heap)
            index = item[1]
            classes[index][0] += 1
            classes[index][1] += 1

            tmp = (classes[index][0] + 1) / (classes[index][1] + 1) - (classes[index][0] / classes[index][1])
            item = (-tmp, index)
            heapq.heappush(max_heap, item)
        
        sumRatio = 0
        for i in range(m):
            sumRatio += classes[i][0] / classes[i][1]
        
        return sumRatio / m

        

s = Solution()
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(s.maxAverageRatio(classes, extraStudents))
