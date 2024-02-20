import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


m, n = list(map(int, input().split()))


for i in range(m, n+1):
    if is_prime(i):
        print(i)
