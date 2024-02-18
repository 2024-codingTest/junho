a, b, c = map(int, input().split())

re1 = (a + b) % c
re2 = ((a % c) + (b % c)) % c
re3 = (a * b) % c
re4 = ((a % c) * (b % c)) % c

print(re1)
print(re2)
print(re3)
print(re4)
