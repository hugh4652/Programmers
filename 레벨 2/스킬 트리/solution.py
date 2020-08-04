def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        learn = ""
        for _skill in skill_tree:
            if (_skill in skill):
                learn += _skill
        check = True
        for i in range(len(learn)):
            if(learn[i] != skill[i]):
                check = False
                break
        if(check): answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))