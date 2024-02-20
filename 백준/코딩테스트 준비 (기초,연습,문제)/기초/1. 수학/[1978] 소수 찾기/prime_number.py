import sys
import math

input = sys.stdin.readline

n = int(input())

prime_numbers = list(map(int, input().split()))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0

for i in prime_numbers:
    if is_prime(i):
        count += 1

print(count)