import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque()

for i in range(n):
    arr.append(i + 1)

flag = 1
while flag:
    if len(arr) == 1:
        print(arr[0])
        break
    else:
        arr.popleft()
        num = arr.popleft()
        arr.append(num)

