def solution(n):
    answer = ""
    digit = "124"
    if(n < 4):
        return digit[n - 1]
    return solution((n-1) // 3) + digit[n % 3 - 1]