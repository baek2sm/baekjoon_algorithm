import sys


def search(n, m, time_list):
    # 마지막 아이가 타기 직전의 시간과 그때까지 몇 명이 탔는지 계산
    f, l = 0, n * max(time_list)
    max_numb, max_min = 0, 0
    while f <= l:
        mid = (f+l) // 2
        numb = sum([(mid-1) // time + 1 for time in time_list])
        if numb < n:
            f = mid + 1
            max_numb = numb
            max_min = mid
        else:
            l = mid - 1

    # 마지막 아이가 몇 번째 놀이기구에 탈지 확인
    for i, time in enumerate(time_list):
        if max_min % time == 0:
            max_numb += 1
            if max_numb == n:
                return i+1


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    time_list = list(map(int, sys.stdin.readline().split()))
    answer = search(n, m, time_list)
    print(answer)
