def solution(numbers, hand):
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    hand_position = ['*', '#']

    position = {
        1: (0, 0), 2: (0, 1), 3:(0, 2),
        4: (1, 0), 5: (1, 1), 6:(1, 2),
        7: (2, 0), 8: (2, 1), 9:(2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2),
    }

    result = ''
    for num in numbers :
        if num in left_key:
            #왼손
            result += 'L'
            hand_position[0] = num
        elif num in right_key:
            #오른손
            result += 'R'
            hand_position[1] = num
        else :
            #더가까운손
            near_hand = get_near_hand(position, hand_position[0], hand_position[1], num, hand)
            if near_hand == 'L' :
                #왼손
                result += 'L'
                hand_position[0] = num
            else :
                #오른손
                result += 'R'
                hand_position[1] = num

    return result

def get_near_hand(position, l, r, num, hand) :
    left_distance = abs(position[l][0] - position[num][0]) + abs(position[l][1] - position[num][1])
    right_distance = abs(position[r][0] - position[num][0]) + abs(position[r][1] - position[num][1])

    #거리가 동일하면 hand값에 따라 반환
    if left_distance == right_distance :
        near_hand = 'L' if hand == 'left' else 'R'
    else :
        #더가까운손
        near_hand = 'L' if left_distance < right_distance else 'R'
    return near_hand