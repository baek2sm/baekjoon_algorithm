import sys


def greedy(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return min(4, (m+1)//2)
    else:
        if m <= 6:
            return min(4, m)
        else:
            return m-2


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    answer = greedy(n, m)
    print(answer)