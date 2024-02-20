# [17425번] 약수의 합

# 문제
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다.  
예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다.  
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다.  
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.  
자연수 N이 주어졌을 때, g(N)을 구해보자.  

# 입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 100,000)가 주어진다.  
둘째 줄부터 테스트 케이스가 한 줄에 하나씩 주어지며 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
각각의 테스트 케이스마다, 한 줄에 하나씩 g(N)를 출력한다.  

# 예제 입력 1
```python
5
1
2
10
70
10000
```  

# 예제 출력 1
```python
1
4
87
4065
82256014
```

# 풀이

## 실패 코드 1 (시간 초과)
```python
import sys

input = sys.stdin.readline

def sum_total_measure(n):
    result = 0

    for i in range(1, n+1):
        result += get_measure_sum(i)

    return result

def get_measure_sum(n):
    measure = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            measure.append(i)

    return sum(measure)


t = int(input())

for i in range(t):
    n = int(input())

    print(sum_total_measure(n))
```  
먼저 `get_measure_sum()` 메서드를 구현해서 n의 약수를 구하고, 그 합을 구하도록 했다.  
`sum_total_measure()`에서는 n까지 반복문을 돌면서, result에 각 수들의 약수의 합을 더하도록 했다.  
그 결과, 각 약수들의 합의 총 합을 구할 수 있었지만 **시간 초과**가 발생했다.  

## 성공 코드 (DP 이용)
