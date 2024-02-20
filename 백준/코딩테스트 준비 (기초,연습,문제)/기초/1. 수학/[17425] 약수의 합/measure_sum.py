import sys

input = sys.stdin.readline

def sum_total_measure(n):
    result = 0

    for i in range(1, n+1):
        result += get_measure_sum(i)

    return result

def get_measure_sum(n):
    measure = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            measure.append(i)

    return sum(measure)


t = int(input())

for i in range(t):
    n = int(input())

    print(sum_total_measure(n))