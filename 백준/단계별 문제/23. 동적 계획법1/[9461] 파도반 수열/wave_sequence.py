import sys

input = sys.stdin.readline

def wave_sequence(num):
    dp = [0 for _ in range(101)]

    # 초기값 초기화
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, 101):
        dp[i] = dp[i-3] + dp[i-2]

    return dp[num]


n = int(input())

arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())
    print(wave_sequence(arr[i]))