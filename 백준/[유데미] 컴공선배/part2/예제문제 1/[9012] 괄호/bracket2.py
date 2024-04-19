import sys

input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    stk = []
    for j in input():
        if j == '(':
            stk.append(j)
        elif j == ')':
            if stk:
                stk.pop()
            else:
                result.append("NO")
                break
        else:
            if stk:
                result.append("NO")
            else:
                result.append("YES")


for i in result:
    print(i)