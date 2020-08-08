import math

def solution(w,h):
    every = w * h
    gcd = math.gcd(w,h)
    return every - (w + h - gcd)

print(solution(8, 12))