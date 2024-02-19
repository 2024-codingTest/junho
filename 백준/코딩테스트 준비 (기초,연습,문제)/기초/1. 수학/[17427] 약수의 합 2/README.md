# [17427번] 약수의 합 2

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

## 성공 코드
```python
import sys

input = sys.stdin.readline

n = int(input())

result = 0
for i in range(1, n+1):
    result += (n//i)*i

print(result)

```  
수학적인 개념을 생각해봐야했다.  
약수를 구하는 방법은 아래와 같다.  
1. 자연수 N이 주어졌을 때, 1부터 N까지 나누어가면서 나머지가 0인 값을 구하는 방법. -> 기존에 내가 썼던 방법  
2. 자연수 N이 주어졌을 때, 약수는 서로 `대칭구조`를 이루고 있으므로, 1부터 √A 까지의 약수를 구하는 방법.  
<br>

하지만, 문제에서 제시한 시간 제한은 1초이다.  
위 방법의 시간 복잡도는 각각 O(n^2), O(n√n)이므로 사용하면 안된다.  
<br>

다른 방법을 생각해야 하는데, 이걸 생각하지 못해 블로그를 참고했다.  
예를 들어, 3의 배수는 3, 6, 9 ... 와 같고, 3의 배수는 3을 약수로 갖는다.  
다른 자연수 또한 마찬가지더라..  

즉, `N 이하의 자연수 중에서 i를 약수로 갖는 개수는 N/i개` 이다.  
```python
g(N) = 1*(N/1) + 2*(N/2) + ... + N*(N/N)
```  
이 방식의 시간복잡도는 `O(n)`이다.  
이 방식을 사용하면 시간제한에 걸리지 않고 성공 코드를 작성할 수 있다.  

*나중에 다시 해봐야겠다.*  