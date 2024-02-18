# [10430번] 나머지

# 문제
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?  
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.  

# 입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)  

# 출력
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.  

# 예제 입력 1
```python
5 8 4
```  

# 예제 출력 1
```python
1
1
0
0
```

# 풀이
```python
a, b, c = map(int, input().split())

re1 = (a + b) % c
re2 = ((a % c) + (b % c)) % c
re3 = (a * b) % c
re4 = ((a % c) * (b % c)) % c

print(re1)
print(re2)
print(re3)
print(re4)

```