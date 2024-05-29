# [10986] 나머지 합 구하기

# 문제
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.  

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.    

# 입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)  

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)  

# 출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.


# 예제 입력 1
```python
5 3
1 2 3 1 2
```

# 예제 출력 1
```python
7
```

# 수도 코드
```python
n, m 입력
A <- 배열 입력

S 합 배열 선언
C 배열 선언

for i -> 1 ~ n - 1:
    S[i] = S[i-1] + A[i] # 합 배열 공식 이용해 저장

for i -> 0 ~ n - 1:
    remain = S[i] % m # 나머지 저장
    if remain == 0:
        answer += 1
    C[remain] += 1 # 나머지 값에 해당하는 인덱스의 값을 증가


for i -> 0 ~ m - 1:
    answer += C[i] 에서 2가지를 뽑는 경우의 수
```

# 내 코드
```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i - 1] + A[i] # 합 배열

for i in range(n):
    remain = S[i] % m
    if remain == 0:
        answer += 1
    C[remain] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)
```
- 합 배열 공식 `S[i] = S[i-1] + A[i]` 를 이용해 합 배열을 구한다.
  - for i in range(1, n) 이므로, 이 전에 S[0]값을 A[0]으로 초기화
- 합 배열의 값을 m으로 나눈 나머지 값으로 치환
- 만약 나머지가 0이면 answer += 1 -> 예를 들어 구간이 (3, 3)인 것처럼 제자리인 경우 인거임
- 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 구함
  - 3C2, 2C2 같은 연산임
  - 나머지 값으로 치환된 S에 대해서 S[i] == S[j] 이면, (A[i+1] + ... + A[j])/m == 0인 구간
  - 즉, 나머지 값으로 치환된 S에 대해서 S[i] == S[j] 이면 원본 리스트에서 i+1 ~ j 까지의 구간 합이 m으로 나누어 떨어지는 구간