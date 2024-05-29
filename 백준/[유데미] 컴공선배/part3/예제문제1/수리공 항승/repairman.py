import sys

input = sys.stdin.readline

n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()

coord = [False] * 1001  # 물이 새는 곳의 위치는 100보다 작거나 같은 자연수

for i in hole:
    coord[i] = True

x = 0
ans = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += l # 테아프를 쓰고나면 테이프 길이만큼 점프
    else:
        x += 1

print(ans)