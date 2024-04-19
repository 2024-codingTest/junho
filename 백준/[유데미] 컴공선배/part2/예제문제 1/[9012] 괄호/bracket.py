import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    is_vps = True
    stk = []
    for j in input():
        if j == '(':
            stk.append(j)
        elif j == ')':
            if stk:
                stk.pop()
            else:
                is_vps = False
                break # stk의 size가 0인데, pop을 하려고 하니, 여기서 멈춰줘야 함

    if stk:
        is_vps = False

    print("YES" if is_vps else "NO")

