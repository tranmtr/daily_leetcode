from typing import List
from collections import deque

def find_left_boundary(arr, target):
    left, right = 0, len(arr) - 1
    result_index = len(arr) 
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= target:
            result_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return result_index


def find_right_boundary(arr, target):
    left, right = 0, len(arr) - 1
    result_index = len(arr)
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] > target:
            result_index = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return result_index

class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.queue_packet = deque()             #(source: int, destination: int, timestamp: int)
        self.set_packet = set()                 #(source: int, destination: int, timestamp: int)
        self.dict_destination = dict()          #(destination: int, list: (timestamp: int))

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        value = (source, destination, timestamp)
        if (value in self.set_packet):
            return False
        
        if (len(self.queue_packet) == self.memory_limit):
            tmp = self.queue_packet.popleft()
            self.set_packet.discard(tmp)
            self.dict_destination[tmp[1]].pop(0)

        self.queue_packet.append(value)
        self.set_packet.add(value)

        if (destination not in self.dict_destination):
            self.dict_destination[destination] = []
        self.dict_destination[destination].append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if (self.queue_packet):
            tmp = self.queue_packet.popleft()
            self.set_packet.discard(tmp)
            self.dict_destination[tmp[1]].pop(0)
            return list(tmp)
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dict_destination:
            return 0
        arr = self.dict_destination[destination]
        head = find_left_boundary(arr, startTime)
        tail = find_right_boundary(arr, endTime)
        return tail - head