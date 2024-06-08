import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

for i in arr:
    print(i)