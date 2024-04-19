# [1302] 베스트셀러

# 문제
김형택은 탑문고의 직원이다.  
김형택은 계산대에서 계산을 하는 직원이다.  
김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.  
오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다.  
이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다.  
책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

# 출력
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다.  
만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

# 예제 입력 1
```python
5
top
top
top
top
kimtop
```

# 예제 출력 1
```python
top
```


# 코드
```python
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


```  

# 풀이
```python
for i in title:
    books[i] = title.count(i)
```  
- 책의 제목 별 개수를 `dict` 형태로 저장 -> 예시: {"title1":4}  

```python
best = []
for k, v in books.items():
    if v == max(books.values()):
        best.append(k)
```
- 딕셔너리의 items 중, key와 value를 추출하고, value가 가장 큰 값인 item의 key값을 best 배열에 저장