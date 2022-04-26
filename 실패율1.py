def solution(N, stages):
    #실패율
    dic = {}
    allPlayer = len(stages)
    for i in range(1, N+1):
        notClearPlayer = stages.count(i)
        failRate = notClearPlayer / allPlayer
        dic[i] = failRate
        
        allPlayer -= notClearPlayer
    print(dic)
    
    #실패율 정렬
    dicSort = sorted(dic.items(), key = lambda x : x[1], reverse = True)
    print(dicSort)
    
    #정렬된 실패율 변환
    answer = []
    for i in range(len(dicSort)):
        answer.append(dicSort[i][0])
    
    return answer