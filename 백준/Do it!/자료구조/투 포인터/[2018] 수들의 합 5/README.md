# [2018] 수들의 합 5

# 문제
어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다.  
당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 이때, 사용하는 자연수는 N이하여야 한다.  
예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.  
N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.  


# 입력
첫 줄에 정수 N이 주어진다.

# 출력
입력된 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 출력하시오.

# 예제 입력 1
```python
15
```

# 예제 출력 1
```python
4
```

# 수도 코드
```python
n 입력
count = 1 # 정답 수
start_index, end_index = 1
sum = 1 # 배열이 1부터 시작하니까 최소 값이 1

while end_index != n:
    if sum == n:
        count++
        end_index++
        sum += end_index    
    elif sum > n:
        sum -= start_index
        start_index++
    elif sum < n:
        end_index++
        sum += end_index
```

# 내 코드
```python
import sys

input = sys.stdin.readline

n = int(input())

count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum = sum + end_index

    elif sum > n:
        sum = sum - start_index
        start_index += 1

    elif sum < n:
        end_index += 1
        sum = sum + end_index

print(count)
```
- 정수 n을 입력받으면, 해당 값 만큼 연속된 자연수의 배열이 있다고 생각하자.
  - ex) n = 5 -> arr: [1, 2, 3, 4, 5]
- start_index ~ end_index 까지의 합(sum)이 n과 같으면 count 1 증가 & end_index 1 증가 & sum += end_index
- sum > n 인 경우에는 start_index가 따라와야 하므로 sum -= start_index & 한 칸씩 따라온다는건 1씩 증가임.
- sum < n 인 경우에는 end_index 1 증가 & sum += end_index