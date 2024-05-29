# [11659] 구간 합 구하기 4

# 문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.  

# 입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.    

# 출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.  

# 제한
- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

# 예제 입력 1
```python
5 3
5 4 3 2 1
1 3
2 4
5 5
```

# 예제 출력 1
```python
12
9
1
```

# 내 코드 1 - 틀린 코드
```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
result = []

for i in range(m):
    s, e = map(int, input().split())

    result.append(sum(numbers[s-1:e]))

for i in result:
    print(i)
```
- 합 배열을 만들지 않고, 배열 슬라이싱을 이용함
- 배열 슬라이싱을 한다는건 구간 합을 매번 계산한다는 뜻이고, 이렇게 되면 최악의 경우 1억회 이상의 연산 수행하게 됨 -> 시간 초과

# 내 코드 2 - 정답 코드
```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
_sum = [0]
temp = 0

# 합 배열: S[i] = S[i-1] + A[i]
for i in numbers:
    temp += i
    _sum.append(temp)

# 구간 합: S[j] - S[i-1]
for i in range(m):
    start, end = map(int, input().split())
    print(_sum[end] - _sum[start - 1])
```

# 수도 코드
```python
N, M
numbers 에 숫자 저장
_sum 으로 합 배열 선언

for i in numbers:
    temp += i
    _sum <- temp

for i in M:
    start, end 변수 입력 받음
    result = _sum[e] - _sum[s-1]
    print(result)
```