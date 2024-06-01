import sys

input = sys.stdin.readline

n = int(input())
status = True
stack = []
result = []

check = 1

for i in range(n):
    num = int(input())
    while check <= num:
        stack.append(check)
        result.append("+")
        check += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        status = False

if not status:
    print("NO")
else:
    for i in result:
        print(i)