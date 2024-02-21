# [6588번] 골드바흐의 추측

# 문제
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.  

> 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.  

예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다.  
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.  

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.  

# 입력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.  
각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)  
입력의 마지막 줄에는 0이 하나 주어진다.  

# 출력
각 테스트 케이스에 대해서, n = a + b 형태로 출력한다.  
이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.  
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.  
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.  

# 예제 입력 1
```python
8
20
42
0
```  

# 예제 출력 1
```python
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
```

# 풀이
아이디어는 먼저, `소수를 판별`하고, 그 결과에서 `a + b = n`이 되는 a, b를 전부 구한다음, a가 최소값인 경우를 출력하는 것이었다.  
a가 최소인 값을 왜 출력하냐면, a + b = n이 되기 위해서는 a가 최소인 값이어야 b가 최대인 값이 나오기 때문에, b-a가 최대가 되기 때문이다.  
예를 들어, n = 8인 경우, 소수는 [2, 3, 5, 7]이지만, a + b = 8이 되는 경우는 3 + 5이고, `홀수 소수의 합`이므로 어차피 2는 떨어져나간다.  

아무튼 이렇게 해결하려고 했으나,, 혼자의 힘으로는 해결하지 못했다.  
반드시 나중에 다시 혼자 힘으로 풀어볼 문제로 남겨야겠다.  

## 실패 코드1
```python
import math
import sys

input = sys.stdin.readline

# 에라토스테네스의 체 사용
def get_prime(n):
    m = int(math.sqrt(n))
    arr = [i for i in range(1000001)]
    for i in range(2, m + 1):
        if arr[i]:
            for j in range(i+i, n, i):
                arr[j] = False
    return [i for i in range(2, n) if arr[i]]


n = int(input())
primes = get_prime(n)

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if (primes[i] + primes[j]) == n:
            print(primes[i], primes[j])

```  
`a + b = n`의 형식으로 나타내는 부분에서 어려움을 느꼈다.  

## 성공 코드
```python
import math
import sys

input = sys.stdin.readline

m = int(math.sqrt(1000001))
arr = [1 for i in range(1000001)]
for i in range(2, m + 1):
    if arr[i]:
        for j in range(i + i, m**2, i):
            arr[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(2, m + 1):
            if arr[i] and arr[n - i]:
                print("%d = %d + %d" % (n, i, n - i))
                break

```  

먼저, 위의 for문은 `에라토스테네스의 체` 방식으로 소수를 판별하는 로직이다.  
그 다음, for문을 도는데, arr[i]와 arr[n-1]가 둘 다 True라면, 그 값이 a + b = n을 만족하는 값이다.  
그 때, 가장 처음으로 조건을 만족하는 때의 arr[i]가 최솟값이므로, arr[n-1] - arr[i]는 최댓값이고, 이걸 출력하고 break한다.  