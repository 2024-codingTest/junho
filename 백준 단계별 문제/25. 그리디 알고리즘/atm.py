import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

result = []
count = 0
while len(arr) > 0:
    count += arr.pop()
    result.append(count)

print(sum(result))
