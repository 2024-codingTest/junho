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
6
9
2 7 4 1 5 3
```

# 예제 출력 1
```python
2
```

# 수도 코드
```python
n 입력
m 입력
nums = [] 입력

nums.sort() # 오름차순

start_index = 1
end_index = n - 1
count = 0

while start_index < end_index:
    if nums[start_index] + nums[end_index] < m:
        start_index += 1
    elif nums[start_index] + nums[end_index] > m:
        end_index -= 1
    else:
        count += 1
        start_index += 1
        end_index -= 1

print(count)
```

# 내 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0
start_index = 0
end_index = n - 1

while start_index < end_index:
    if nums[start_index] + nums[end_index] < m:
        start_index += 1
    elif nums[start_index] + nums[end_index] > m:
        end_index -= 1
    else:
        count += 1
        start_index += 1
        end_index -= 1

print(count)
```
