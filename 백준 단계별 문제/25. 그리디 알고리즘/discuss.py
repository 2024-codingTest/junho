import sys
input = sys.stdin.readline

def discuss(arr):
    # 회의 리스트 끝나는 시간 기준 정렬
    sorted_mettings = sorted(arr, key=lambda x:x[1])
    # 결과 리스트
    result_list = []
    # 첫 번째 회의 추가
    result_list.append(sorted_mettings[0])
    # 선택한 회의의 끝나는 시간
    last_end_time = sorted_mettings[0][1]

    for meeting in sorted_mettings[1:]:
        start_time, end_time = meeting
        if(start_time >= last_end_time):
            result_list.append(meeting)
            last_end_time = end_time

    return result_list

# 사용자로부터 입력 받기
n = int(input())  # 회의의 개수
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

result = discuss(meetings)
print(len(result))