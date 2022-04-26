def solution(boards, moves):
    moves = list(map(lambda mv : mv-1, moves))
    stack = [0]
    cnt = 0
    
    for i in moves :
        for board in boards :
            if board[i] != 0 :
                stack.append(board[i])
                board[i] = 0
                if stack[-1] == stack[-2] :
                    stack.pop()
                    stack.pop()
                    cnt += 2
                break    
    
    return cnt