# import sys
# input = sys.stdin.readline
#
# def mySum(arr2):
#     re = 0
#     # -를 기준으로 나눠진 배열의 요소를 +를 기준으로 다시 한 번 나눔
#     sub = arr2.split('+')
#
#     for j in sub:
#         re += int(j)
#
#     return re
#
#
# arr = list(input().split('-'))
# answer = 0
# temp = 0
#
# for i in arr:
#     temp = mySum(i)
#     # i가 첫 번째 요소이면 -를 하면 안되니까
#     if i==arr[0]:
#         answer += temp
#     # i가 첫 번째 요소가 아니면 -를 기준으로 나눈거니까 다 -해줌
#     else:
#         answer -= temp
#
# print(answer)


import sys
input = sys.stdin.readline

arr = list(input().split('-'))
result = []


for i in arr:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum += int(j)
    result.append(sum)

n = result[0]

for i in range(1, len(result)):
    n -= result[i]


print(n)
