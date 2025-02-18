def solution(clothes):
    answer = 1
    closet = {}
    for kind, type in clothes:
        if type not in closet.keys():
            closet[type] = [kind]
        else:
            closet[type] += [kind]
    for key, value in closet.items():
        answer *= (len(value) + 1)
        
    return answer - 1