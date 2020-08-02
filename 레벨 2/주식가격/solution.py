def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if(prices[i] > prices[j]):
                answer[i] += 1
                break
            else:
                answer[i] += 1
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))