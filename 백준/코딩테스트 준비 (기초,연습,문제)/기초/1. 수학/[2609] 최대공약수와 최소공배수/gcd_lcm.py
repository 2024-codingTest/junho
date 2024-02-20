# gcd: 최대공약수
# lcm: 최소공배수

import sys

input = sys.stdin.readline


# 최대공약수: 나누어 떨어질 때 까지 나누기
def gcd(a, b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a

# 최소공배수
def lcm(a, b):
    return (a * b) // gcd(a, b)


n, m = list(map(int, input().split()))


print(gcd(n, m))
print(lcm(n, m))