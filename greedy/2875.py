import sys


def greedy(n, m, k):
    result = 0
    while n+m-3 >= k and n >= 2 and m >= 1:
        result += 1
        n -= 2
        m -= 1
    return result


if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    answer = greedy(n, m, k)
    print(answer)