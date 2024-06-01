import sys

input = sys.stdin.readline

n = int(input())

count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum = sum + end_index

    elif sum > n:
        sum = sum - start_index
        start_index += 1

    elif sum < n:
        end_index += 1
        sum = sum + end_index

print(count)