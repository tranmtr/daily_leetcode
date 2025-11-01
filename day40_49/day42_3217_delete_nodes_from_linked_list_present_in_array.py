# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    # def binarySearch(self, arr, targetVal):
    #     left = 0
    #     right = len(arr) - 1

    #     while left <= right:
    #         mid = left + (right - left) // 2

    #         if arr[mid] == targetVal:
    #             return mid

    #         if arr[mid] < targetVal:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     return -1

    # def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    #     len_nums = len(nums)
    #     nums.sort()
    #     while (head != None):
    #         if (self.binarySearch(nums, head.val) == -1):
    #             break
    #         head = head.next
        
    #     if (head == None):
    #         return head
        
    #     before = head
    #     if (before.next != None):
    #         after = before.next
    #     else:
    #         return head
        
    #     while (before != None and after != None):
    #         if (self.binarySearch(nums, after.val) != -1):
    #             if (after.next == None):
    #                 before.next = None
    #                 return head
    #             else:
    #                 after = after.next
    #                 before.next = after
    #         else:
    #             before = after
    #             if (after.next == None):
    #                 return head
    #             else:
    #                 after = before.next

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        while (head != None):
            if (head.val not in nums_set):
                break
            head = head.next
        
        if (head == None):
            return head
        
        before = head
        if (before.next != None):
            after = before.next
        else:
            return head
        
        while (before != None and after != None):
            if (after.val in nums_set):
                if (after.next == None):
                    before.next = None
                    return head
                else:
                    after = after.next
                    before.next = after
            else:
                before = after
                if (after.next == None):
                    return head
                else:
                    after = before.next
        
        
                        


