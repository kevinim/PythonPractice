#TapeEquilibrium
"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7

Write a function:
def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    Absolute = None                                 #최소값을 처음에는 미정
    for i in range(1, len(A)):              
        A1 = A[:i]                                  #i차례인 N을 기준으로 슬라이싱 했을 때 A1 한쪽
        A2 = A[i:]                                  #i이후부터 A2 다른 한쪽
        result = abs(sum(A1)-sum(A2))               #절대값 Abs 함수로 두 덩어리를 뺌
        if Absolute == None or result < Absolute :
            Absolute = result
    return Absolute
    pass