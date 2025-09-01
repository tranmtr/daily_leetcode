class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        m = len(classes)

        for _ in range(extraStudents):
            indexDiffMax = 0
            diffMax = 0
            for i in range(m):
                tmp = (classes[i][0] + 1) / (classes[i][1] + 1) - (classes[i][0] / classes[i][1])
                if (tmp > diffMax):
                    diffMax = tmp
                    indexDiffMax = i

            classes[indexDiffMax][0] += 1
            classes[indexDiffMax][1] += 1
        
        sumRatio = 0
        for i in range(m):
            sumRatio += classes[i][0] / classes[i][1]

        return round(sumRatio / m, 4)