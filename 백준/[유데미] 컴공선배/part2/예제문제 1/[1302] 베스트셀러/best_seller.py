import sys


input = sys.stdin.readline

title = []
for i in range(int(input())):
    title.append(input())

books = dict()
for i in title:
    books[i] = title.count(i)

best = []
for k, v in books.items():
    if v == max(books.values()):
        best.append(k)

best = sorted(best) # 가장 많이 팔린 책들의 제목을 정렬
print(best[0]) # 그 중 첫 번째 출력

