# [11047] 동전 0

# 문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.  
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.  
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.  
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

# 예제 입력 1
```python
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
```


# 예제 출력 1
```python
6
```

# 내 코드
```python
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append((int(input())))

sorted(coins)
coins.reverse()

# re = []
re = 0
for i in coins:
    if k - i >= 0:
        num = k // i
        # re.append(num)
        re += num
        k -= i * num


# print(sum(re))
print(re)
```  
- 가장 큰 값의 동전부터 해결해야 하니까, 역순 정렬을 해주자!
- re라는 변수 혹은 리스트에 최대 동전 개수를 추가
- 그 값 만큼 k에서 빼고 다시 반복!

# 컴공선배 코드
```python
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.reverse()

ans = 0
for coin in coins:
    ans += k // coin
    k %= coin
    # print(f"coin: {coin}, k: {k}, ans: {ans}")
print(ans)
```  
- k에 coin만큼 나누고 난 후의 나머지를 저장해준다.
  - 4200 % 1000 -> 200
- 중간중간 print를 통한 내 코드의 정상 동작 확인은 좋은 습관!