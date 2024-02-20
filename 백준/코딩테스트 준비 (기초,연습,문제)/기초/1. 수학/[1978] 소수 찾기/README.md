# [1978번] 소수 찾기

# 문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.  

# 입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.  


# 출력
주어진 수들 중 소수의 개수를 출력한다.  

# 예제 입력 1
```python
4
1 3 5 7
```  

# 예제 출력 1
```python
3
```

# 풀이
`소수(Prime Number)`는 1과 자기 자신만 약수로 갖는 2이상의 자연수를 뜻한다.  
소수를 구하려면 1과 자기 자신만 나누어 떨어져야 하므로 2부터 n까지의 for문을 돌아 나누어 떨어지는지를 확인하려고 했다.  
```python
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```  
그런데, 약수의 특징 중 하나가 `대칭구조`를 이룬다는 점을 발견했다.  
[예시]  
- 10: 1, 2, 5, 10  
- 25: 1, 5, 25  
- 28: 1, 2, 4, 7, 14, 28  
...  

이렇게 대칭구조를 갖는데, 대칭의 축이 되는 부분의 근삿값은 n의 제곱근으로 생각할 수 있다.  
즉, 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, n의 제곱근까지만 확인하면 된다는 것이다.  
`import math`의 `sqrt(n)`을 적용해 제곱근 값을 구하고, 제곱근 값을 포함한 범위까지 반복해야 하므로 1을 더한 지점까지 for문을 반복한다.  



## 성공 코드
```python
import sys
import math

input = sys.stdin.readline

n = int(input())

prime_numbers = list(map(int, input().split()))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0

for i in prime_numbers:
    if is_prime(i):
        count += 1

print(count)
```  
