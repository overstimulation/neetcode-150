import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        indexed_tasks.sort()

        res = []
        min_heap = []
        i = 0
        time = 0
        n = len(tasks)

        while i < n or min_heap:
            if not min_heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= time:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1

            proc_time, index = heapq.heappop(min_heap)
            time += proc_time
            res.append(index)

        return res
