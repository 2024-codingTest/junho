n = int(input())
scores = list(map(int, input().split()))

m = max(scores)

_sum = sum(scores)

print((_sum / m * 100) / int(n))
