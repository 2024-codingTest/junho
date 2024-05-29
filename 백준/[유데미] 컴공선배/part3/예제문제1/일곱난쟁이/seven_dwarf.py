import sys
from itertools import combinations

input = sys.stdin.readline

arr = []
for i in range(9):
    num = int(input())
    if num >= 100:
        break
    else:
        arr.append(num)

re = []
for i in combinations(arr, 7):
    if sum(i) == 100:
        for a in sorted(i):
            print(a)
        break
