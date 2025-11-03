from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ballon = colors[0]
        max_time = neededTime[0]
        result = 0
        len_colors = len(colors)

        for i in range(1, len_colors):
            if (colors[i] == ballon):
                if max_time < neededTime[i]:
                    result += max_time
                    max_time = neededTime[i]
                else:
                    result += neededTime[i]
            else:
                ballon = colors[i]
                max_time = neededTime[i]
        
        return result
