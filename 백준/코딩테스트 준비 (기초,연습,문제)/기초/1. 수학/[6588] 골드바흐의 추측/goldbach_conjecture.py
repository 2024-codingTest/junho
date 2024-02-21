# import math
# import sys
#
# input = sys.stdin.readline
#
# m = int(math.sqrt(1000001))
# arr = [1 for i in range(1000001)]
# for i in range(2, m + 1):
#     if arr[i]:
#         for j in range(i + i, m + 1, i):
#             arr[j] = False
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         for i in range(2, m + 1):
#             if arr[i] and arr[n - i]:
#                 print("%d = %d + %d" % (n, i, n - i))
#                 break


import math
import sys

input = sys.stdin.readline

m = int(math.sqrt(1000001))
arr = [1 for i in range(1000001)]
for i in range(2, m + 1):
    if arr[i]:
        for j in range(i + i, m**2, i):
            arr[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(2, m + 1):
            if arr[i] and arr[n - i]:
                print("%d = %d + %d" % (n, i, n - i))
                break