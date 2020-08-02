import operator as op
from functools import reduce

def solution(n):
    answer = 0
    j = 0
    for i in range(n, -1, -2):
        answer += nCr(i + j, j)
        j += 1
    return answer % 1000000007


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


