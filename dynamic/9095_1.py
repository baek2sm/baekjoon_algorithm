import sys


memoization = None
def search(n):
    if memoization[n-1]:
        return memoization[n-1]

    result = search(n-1) + search(n-2) + search(n-3)
    memoization[n-1] = result
    return result


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    answer_list = []
    for i in range(t):
        n = int(sys.stdin.readline())
        memoization = list([1, 2, 4] + [0 for _ in range(n)])[:n]
        answer_list.append(search(n))

    for answer in answer_list:
        print(answer)