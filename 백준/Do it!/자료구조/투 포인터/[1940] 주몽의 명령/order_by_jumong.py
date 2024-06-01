import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0
start_index = 0
end_index = n - 1

while start_index < end_index:
    if nums[start_index] + nums[end_index] < m:
        start_index += 1
    elif nums[start_index] + nums[end_index] > m:
        end_index -= 1
    else:
        count += 1
        start_index += 1
        end_index -= 1

print(count)