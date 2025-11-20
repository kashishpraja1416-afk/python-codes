# P11: Calculate Duration Between Two Times
N = int(input())

for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())

    start_minutes = SH * 60 + SM
    end_minutes = EH * 60 + EM

    if end_minutes < start_minutes:
        end_minutes += 24 * 60

    duration = end_minutes - start_minutes
    hours = duration // 60
    minutes = duration % 60

    print(hours, minutes)
