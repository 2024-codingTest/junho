# [1427] 소트인사이드

# 문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.


# 예제 입력 1
```python
2143
```

# 예제 출력 1
```python
4321
```


# 내 코드
```python
import sys

input = sys.stdin.readline

A = list(input())

for i in range(len(A)):
    max_ = i
    for j in range(i+1, len(A)):
        if A[j] > A[max_]:
            max_ = j
    if A[i] < A[max_]:
        temp = A[i]
        A[i] = A[max_]
        A[max_] = temp

for i in range(len(A)):
    print(A[i], end="")
```
- `선택 정렬`을 사용한다.
- 내림차순으로 정렬하니까, 최댓값을 찾는다!
- 최댓값을 찾고, 0번 인덱스부터 증가해가면서 최댓값을 찾으면 swap한다!
- 위 과정을 반복하면서 내림차순으로 정렬한다.