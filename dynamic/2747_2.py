import sys


def fibonacci(n):
    if n <= 1:
        return n

    memoization = [0, 1]
    for i in range(2, n+1):
        memoization.append(memoization[i-1] + memoization[i-2])
    return memoization[n]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    answer = fibonacci(n)
    print(answer)