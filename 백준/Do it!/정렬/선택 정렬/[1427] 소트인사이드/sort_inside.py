import sys

input = sys.stdin.readline

A = list(input())

for i in range(len(A)):
    max_ = i
    for j in range(i+1, len(A)):
        if A[j] > A[max_]:
            max_ = j
    if A[i] < A[max_]:
        temp = A[i]
        A[i] = A[max_]
        A[max_] = temp

for i in range(len(A)):
    print(A[i], end="")