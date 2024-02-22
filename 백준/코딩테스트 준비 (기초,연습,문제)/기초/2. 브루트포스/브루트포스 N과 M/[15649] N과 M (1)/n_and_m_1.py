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