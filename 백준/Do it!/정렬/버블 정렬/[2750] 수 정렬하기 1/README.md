# [2750] 수 정렬하기 1

# 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.  
둘째 줄부터 N개의 줄에는 수가 주어진다.  
이 수는 절댓값이 1,000보다 작거나 같은 정수이다.  
수는 중복되지 않는다.

# 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


# 예제 입력 1
```python
5
5
2
3
4
1
```

# 예제 출력 1
```python
1
2
3
4
5
```


# 내 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

for i in arr:
    print(i)
```
- 버블 정렬을 이용한다.
- 이중 for문을 사용하고, `for i in range(n-1)`과 `for j in range(n-1-i)`만큼 반복하며 수를 비교한다.