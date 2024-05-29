import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append((int(input())))

sorted(coins)
coins.reverse()

# re = []
re = 0
for i in coins:
    if k - i >= 0:
        num = k // i
        # re.append(num)
        re += num
        k -= i * num


# print(sum(re))
print(re)