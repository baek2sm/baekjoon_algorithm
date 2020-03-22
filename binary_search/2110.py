import sys


def search(pos_list, c):
    result = 0
    f, l = 1, max(pos_list)
    while f <= l:
        mid = (f + l)//2
        if check(pos_list, c, mid):
            f = mid + 1
            result = mid
        else:
            l = mid - 1
    return result


def check(pos_list, c, meter):
    result = 1
    last_pos = pos_list[0]
    for pos in pos_list:
        if pos - last_pos >= meter:
            result += 1
            last_pos = pos
    return result >= c


if __name__ == '__main__':
    n, c = map(int, sys.stdin.readline().split())
    pos_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    pos_list = sorted(pos_list)
    answer = search(pos_list, c)
    print(answer)