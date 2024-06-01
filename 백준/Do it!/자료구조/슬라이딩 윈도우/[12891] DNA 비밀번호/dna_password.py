import sys
input = sys.stdin.readline

# 입력 받기
s, p = map(int, input().split())
dna = input().strip()
a, c, g, t = map(int, input().split())

required = {'A': a, 'C': c, 'G': g, 'T': t}
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(p):
    current[dna[i]] += 1

count = 0

def is_valid():
    return all(current[char] >= required[char] for char in 'ACGT')

if is_valid():
    count += 1

for i in range(p, s):
    current[dna[i]] += 1
    current[dna[i - p]] -= 1
    if is_valid():
        count += 1

print(count)
