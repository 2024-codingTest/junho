import sys

input = sys.stdin.readline

arr = [0 for i in range(9)]

for i in range(9):
    arr[i] = int(input())

sum_re = sum(arr)

fake = []
for i in range(9):
    for j in range(i+1, 9):
        if len(fake) == 2:
            continue
        if sum_re - arr[i] - arr[j] == 100:
            fake.append(arr[i])
            fake.append(arr[j])

arr.sort()
for i in arr:
    if i in fake:
        continue
    print(i)