from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        arrayIndexZero = [-1]
        res = 0

        for i in range(length):
            if (nums[i] == 0):
                arrayIndexZero.append(i)

        arrayIndexZero.append(length) # Chan 1 o cuoi
        lenZero = len(arrayIndexZero)

        if (lenZero == 1 or lenZero == 2):
            return length - 1
        
        for i in range(lenZero - 2):
            res = max(res, arrayIndexZero[i + 2] - arrayIndexZero[i] - 2)
        return res
    
s = Solution()
arr = [1,1,0,0,1,1,1,0,1]
print(s.longestSubarray(arr))