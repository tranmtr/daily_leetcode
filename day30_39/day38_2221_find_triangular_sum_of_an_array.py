from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        while n > k + 1:
            for i in range(n - 1, k, -1):
                nums[i] = (nums[i] + nums[i - 1]) % 10
            k += 1
        return nums[-1]