import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_user = dict()
        self.task_priority = dict()
        self.priority_task = []

        for element in tasks:
            userId = element[0]
            taskId = element[1]
            priority = element[2]

            self.task_user[taskId] = userId
            self.task_priority[taskId] = priority
            heapq.heappush(self.priority_task, (-priority, -taskId))


    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_user[taskId] = userId
        self.task_priority[taskId] = priority
        heapq.heappush(self.priority_task, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_priority[taskId] = newPriority
        heapq.heappush(self.priority_task, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.task_priority[taskId] = -1
        self.task_user[taskId] = -1

    def execTop(self) -> int:
        while (self.priority_task):
            tmp = heapq.heappop(self.priority_task)
            if (-tmp[0] == self.task_priority[-tmp[1]]):
                result = self.task_user[-tmp[1]]
                self.task_priority[-tmp[1]] = -1
                self.task_user[-tmp[1]] = -1
                return result
        return -1