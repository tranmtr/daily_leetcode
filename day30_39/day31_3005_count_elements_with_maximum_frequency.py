from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1
        
        max_frequency = 0
        for x in frequency:
            if frequency[x] > max_frequency:
                max_frequency = frequency[x]
        
        total = 0
        for x in frequency:
            if frequency[x] == max_frequency:
                total += max_frequency
        
        return total