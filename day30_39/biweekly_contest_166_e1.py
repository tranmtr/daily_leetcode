class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        frequency = {}
        group = {}
        for x in s:
            if x not in frequency:
                frequency[x] = 0
            frequency[x] += 1
        
        for key in frequency:
            value = frequency[key]
            if value not in group:
                group[value] = []
            group[value].append(key)
        
        f = -1
        res = []
        
        for key in group:
            if len(group[key]) > len(res):
                res = group[key]
                f = key
            elif len(group[key]) == len(res) and f < key:
                res = group[key]
                f = key
        return ''.join(res)