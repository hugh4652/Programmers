def solution(answers):
    grade = [0, 0, 0]
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, num in enumerate(answers):
        if(student1[i % len(student1)] == num): grade[0] += 1
        if(student2[i % len(student2)] == num): grade[1] += 1
        if(student3[i % len(student3)] == num): grade[2] += 1
        
    maxNum = max(grade)
    answer = list()
    
    for i in range(3):
        if(maxNum == grade[i]):
            answer.append(i + 1)
    
    return answer

print(solution([1, 2, 3, 4, 5]))