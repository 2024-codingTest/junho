# [1929번] 소수 구하기

# 문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.    

# 입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.  
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.  

# 출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.  

# 예제 입력 1
```python
3 16
```  

# 예제 출력 1
```python
3
5
7
11
13
```

# 풀이
**1978번 소수 찾기** 문제와 같은 방식으로 접근했다.  
쓸데없이 m ~ n 까지의 수 중 소수인 수를 list로 받는 짓을 해서 4번인가 오답을 냈다.  
그럴 필요 없이 출력 부분에서 for문으로 돌려주면서 print하기만 하면 되는 문제였다.  

## 성공 코드
```python
import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


m, n = list(map(int, input().split()))


for i in range(m, n+1):
    if is_prime(i):
        print(i)

```  
