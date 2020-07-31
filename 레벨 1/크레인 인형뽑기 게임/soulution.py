board = list(map(list, zip(*board)))

for i in range(0, len(board)):
    while True:
        if(board[i][0] != 0):
            break
        else:
            board[i].pop(0)

stack = list()

for num in moves:
    try:
        stack.append(board[num - 1].pop(0))
    except:
        continue

for i in range(len(stack)):
    basket = list()
    for j in range(0, len(stack) - 1):
        if(stack[j] != stack[j + 1]):
            basket.append(stack[j])
        else:
            answer += 2
            stack.pop(j)
            stack.pop(j)
            break
        
print(answer)
