from typing import List

# class Solution:
#     def binarySearch(self, nums, l, r):
#         tmp = nums[r] -  nums[l]
#         l += 1
#         r -= 1
#         res = -1
#         # print("l = ", l)
#         # print("r = ", r)
#         while (l <= r):
#             m = (r - l) // 2 + l
#             # print("m = ", m)
#             if (nums[m] > tmp):
#                 res = m
#                 r = m - 1
#             else:
#                 l = m + 1
#         return res

#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         cnt = 0
#         for i in range(n - 2):
#             for j in range(n - 1, i + 1, -1):
#                 index = self.binarySearch(nums, i, j)
#                 # print("i = ", i)
#                 # print("j = ", j)
#                 # print("index = ", index)
#                 if index == -1:
#                     continue
#                 cnt += (j - index)
#         return cnt


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[j] + nums[i] > nums[k]:
                    cnt += (j - i)
                    j -= 1
                else:
                    i += 1
        return cnt
S = Solution()
nums = [2,2,3,4]
print(S.triangleNumber(nums))
