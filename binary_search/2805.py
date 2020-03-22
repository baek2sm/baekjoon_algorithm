import sys


def search(height_list, m):
    result = 0
    f, l = 0, max(height_list)
    while f <= l:
        mid = (f + l)//2
        if check(height_list, m, mid):
            f = mid + 1
            result = mid
        else:
            l = mid - 1

    return result


def check(height_list, m, h):
    meter = sum([height - h for height in height_list if height > h])
    return meter >= m


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    height_list = list(map(int, sys.stdin.readline().split()))
    answer = search(height_list, m)
    print(answer)