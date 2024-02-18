import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

if(len(arr) == n):
    print(max(arr) * min(arr))
else:
    print('')