def isValid(c):
    if c.isalnum():
        return True
    if c == '-' or c == '_' or c == '.':
        return True
    return False

def solution(new_id):
    answer = ''

    lastDot = False

    for ch in new_id:
        if isValid(ch) == False:
            continue

        if ch == '.':
            if len(answer) == 0 or lastDot:
                continue
            lastDot = True
        else:
            lastDot = False

        ch = ch.lower()
        answer += ch

    if len(answer) >= 16:
        answer = answer[:15]

    if answer.endswith('.'):
        answer = answer[:-1]

    if len(answer) == 0:
        answer += 'a'

    if len(answer) <= 2:
        ch = answer[-1:]
        while len(answer) < 3:
            answer += ch

    return answer