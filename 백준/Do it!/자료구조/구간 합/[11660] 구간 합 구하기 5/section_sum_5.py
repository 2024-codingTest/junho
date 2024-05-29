import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# nums = [[0] * (n+1)]
nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))
    # nums.append(([0] + [int(x) for x in input().split()]))

dp = [[0] * (n + 1) for _ in range(n + 1)] # 1부터 시작하기 때문
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + nums[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

