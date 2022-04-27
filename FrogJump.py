"""
A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position greater than or equal to Y.
The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:
def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""

def solution(X, Y, D):
    distance = Y-X
    Q = distance//D          # 몫
    R = distance%D           # 나머지
    if R == 0:
    	return Q
    elif R != 0:       # R != 0 이것도 상관없을 듯 합니다
    	return Q+1

# 1. 도착지까지의 실질적인 거리는 Y - X이기 때문에 이를 destination 변수에 저장
# 2. 만약, destination에서 D를 나눴을 때의 나머지가 0이 아니라면 1번을 더 가야하기 때문에
# (destination / D) + 1,
# D를 나눴을 때 나머지가 0이라면 
# (destination / D)를 jumps 변수에 저장합니다.