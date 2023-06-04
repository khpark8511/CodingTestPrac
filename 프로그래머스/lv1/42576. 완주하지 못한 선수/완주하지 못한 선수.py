def solution(participant, completion):
    answer = dict()
    cnt = 0
    for i in participant:
        answer[i] = 0
    for i in participant:
        answer[i] += 1 
    #print(answer)
    for i in completion:
        answer[i] -= 1 
    for i in answer.keys():
        if answer[i] != 0 : 
           return i 