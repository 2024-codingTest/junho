import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
_sum = [0]
temp = 0

# 합 배열: S[i] = S[i-1] + A[i]
for i in numbers:
    temp += i
    _sum.append(temp)

# 구간 합: S[j] - S[i-1]
for i in range(m):
    start, end = map(int, input().split())
    print(_sum[end] - _sum[start - 1])