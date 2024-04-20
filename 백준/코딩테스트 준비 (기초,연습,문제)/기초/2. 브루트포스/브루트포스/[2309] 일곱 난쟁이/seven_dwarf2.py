import sys
from itertools import combinations

input = sys.stdin.readline

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))


for i in combinations(dwarfs, 7):
    if sum(i) == 100:
        for a in sorted(i):
            print(a)
        break
