import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    result = 0
    i, j = list(map(int, input().split()))
    while (i <= j):
        result += arr[i-1]
        i += 1

    print(result)
