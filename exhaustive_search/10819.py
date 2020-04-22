import sys
from itertools import permutations


def search(A_array):
    result = 0
    for A in A_array:
        sum_of_values = 0
        for i in range(len(A)-1):
            sum_of_values += abs(A[i] - A[i+1])
        if result < sum_of_values:
            result = sum_of_values
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A_array = list(permutations(map(int, sys.stdin.readline().split())))
    answer = search(A_array)
    print(answer)