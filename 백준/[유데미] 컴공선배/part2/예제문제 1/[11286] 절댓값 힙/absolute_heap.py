import sys
import heapq as hq

input = sys.stdin.readline

arr = []

for i in range(int(input())):
    n = int(input())
    if n:
        hq.heappush(arr, (abs(n), n))
    else:
        if arr:
            print(hq.heappop(arr)[1])
        else:
            print(0)