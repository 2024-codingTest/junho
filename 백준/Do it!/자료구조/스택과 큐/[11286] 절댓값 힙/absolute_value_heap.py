# import sys
# from queue import PriorityQueue

# input = sys.stdin.readline

# n = int(input())
# q = PriorityQueue()

# answer = []

# for i in range(n):
#     num = int(input())
#     if num == 0:
#         if q.empty():
#             answer.append(0)
#         else:
#             temp = q.get()
#             answer.append(temp[1])
#     else:
#         q.put((abs(num), num))

# for i in answer:
#     print(i)

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
answer = []

for _ in range(n):
    num = int(input())
    if num == 0:
        try:
            answer.append(heapq.heappop(heap)[1])
        except:
            answer.append(0)
    else:
        heapq.heappush(heap, (abs(num), num))

for i in answer:
    print(i)
