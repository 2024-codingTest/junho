# [9012] 괄호

# 문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.  
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.  
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.  
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

# 출력
입력 데이터는 표준 입력을 사용한다.  
입력은 T개의 테스트 데이터로 주어진다.  
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.    
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.  
하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

# 예제 입력1
```python
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
```

# 예제 출력1
```python
NO
NO
YES
NO
YES
NO
```

# 코드1
```python
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    is_vps = True
    stk = []
    for j in input():
        if j == '(':
            stk.append(j)
        elif j == ')':
            if stk:
                stk.pop()
            else:
                is_vps = False
                break # stk의 size가 0인데, pop을 하려고 하니, 여기서 멈춰줘야 함

    if stk:
        is_vps = False

    print("YES" if is_vps else "NO")


```

# 코드2
```python
import sys

input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    stk = []
    for j in input():
        if j == '(':
            stk.append(j)
        elif j == ')':
            if stk:
                stk.pop()
            else:
                result.append("NO")
                break
        else:
            if stk:
                result.append("NO")
            else:
                result.append("YES")


for i in result:
    print(i)
```