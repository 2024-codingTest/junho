# [1978번] 소수 찾기

# 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열  

# 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)  

# 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.  
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.  

# 예제 입력 1
```python
3 1
```  

# 예제 출력 1
```python
1
2
3
```

# 예제 입력 2
```python
4 2
```  

# 예제 출력 2
```python
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
```

# 풀이
**아이디어**  
- 1부터 N중에 하나를 선택
- 다음 1부터 N까지 선택할 때, 이미 선택한 값이 아닌 경우를 선택 (방문 여부 확인)  
- M개를 선택할 경우 print
<br>

**시간복잡도**  
- N^N: 중복이 가능, N=8까지 가능
- N!: 중복이 불가능, N=10까지 가능
<br>

**자료구조**  
- 방문 여부 확인 배열: bool[]
- 선택한 값 입력 배열: int[] 

## 코드
```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []
check = [False] * (n + 1) # n개로 하게되면, False가 n개인 배열이 됨 ->
                          # 인덱스에 바로 접근하게 하려면 check[0]은 사용하지 않고, 바로 1부터 사용

def recur(num):
    if num == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recur(num + 1)
            check[i] = False
            result.pop()

recur(0)
```