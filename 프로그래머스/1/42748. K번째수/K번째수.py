def solution(array, commands):
    answer = []
    
    for com in commands:
        sorting = array[com[0]-1:com[1]]
        sorting = sorted(sorting)
        finals = sorting[com[2]-1]
        answer.append(finals)
    
    return answer