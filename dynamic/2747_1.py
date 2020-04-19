import sys

memoization = None
def fibonacci(n):
    if n <= 1:
        return n
    else:
        if memoization[n] > 1:
            return memoization[n]
        memoization[n] = fibonacci(n-1) + fibonacci(n-2)
        return memoization[n]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    memoization = [0 for _ in range(n+1)]
    answer = fibonacci(n)
    print(answer)