import sys


def greedy(k, coins):
    result = 0
    for i in range(n - 1, -1, -1):
        if k >= coins[i]:
            result += k // coins[i]
            k = k % coins[i]
    return result


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline()) for _ in range(n)]
    answer = greedy(k, coins)
    print(answer)