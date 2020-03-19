import sys


def search(k_list, n):
    f, l = 1, max(k_list)
    result = 0
    while f <= l:
        mid = (f+l) // 2
        if check(k_list, mid, n):
            f = mid + 1
            result = mid
        else:
            l = mid - 1
    return result


def check(k_list, meter, n):
    cnt = sum([k_meter // meter for k_meter in k_list])
    return cnt >= n


if __name__ == '__main__':
    k, n = map(int, sys.stdin.readline().split())
    k_list = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
    answer = search(k_list, n)
    print(answer)