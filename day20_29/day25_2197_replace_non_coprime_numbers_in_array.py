from typing import List
import math

# class Solution:
#     def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
#         len_nums = len(nums)
#         i = 0
#         while ( i < len_nums - 1):
#             if (math.gcd(nums[i], nums[i + 1]) != 1):
#                 nums[i] = math.lcm(nums[i], nums[i + 1])
#                 nums.pop(i + 1)
#                 len_nums -= 1
#                 if (i == 0):
#                     i -= 1
#                 else:
#                     i -= 2
#             i += 1
#         return nums

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        stack = [nums[0]]
        for i in range(1, len_nums):
            if (math.gcd(stack[-1], nums[i]) == 1):
                stack.append(nums[i])
            else:
                stack[-1] = math.lcm(stack[-1], nums[i])
                while (len(stack) > 1 and math.gcd(stack[-1], stack[-2]) != 1):
                    stack[-2] = math.lcm(stack[-1], stack[-2])
                    stack.pop()
        return stack

            
S = Solution()
nums = [6,4,3,2,7,6,2]
print(S.replaceNonCoprimes(nums))