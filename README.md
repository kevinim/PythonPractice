# PythonPractice

1. 정규표현식

"어떤 문자열의 규칙을 찾아서 어떠한 조건과 일치하는 문자열을 다른 것으로 바꾸어라." 이런 유형의 문제를 처리할 때 쓰이는 방법

**문자 클래스 []**

_[abc]_

- [] 사이의 문자들과 매치
- "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
- "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
- "dude"는 정규식과 일치하는 a, b, c증 어느 하나도 포함하고 있지 않으므로 매치되지 않음
- 하이픈을 사용하여 From-To로 표현 가능
  - Ex) [a-c] = [abc], [0-5] = [012345]

**Dot(.)**

_a.b_

- 줄바꿈(\n)을 제외한 모든 문자와 매치
- "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
- "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
- "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다

**반복(*)**
**반복(+)**

_ca*t_

- "ct"는 "a"가 0번 반복되어 매치
- "cat"는 "a"가 0번 이상 반복되어 매치 (1번 반복)
- "caaat"는 "a"가 0번 이상 반복되어 매치 (3번 반복)



