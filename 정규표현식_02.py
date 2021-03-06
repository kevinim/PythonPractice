import re
p = re.compile('[a-z]+')

"""
m = p.match('3 python')
# python의 경우 match object를 return 하지만
# 3 python의 경우 None으로 나옴

m = p.search('3 python')
# python의 경우 위와 동일한 match object를 return 함
# 3 python의 경우 span=(2,8) 부분적일치하느 부분 알려줌

m = p.findall('life is too short')
# 문장의 경우 ['life', 'is', 'too', 'short'] 일치하는 소문자 스트링을 돌려줌

m = p.finditer('life is too short')
# finditer의 경우 이터레이션 값을 돌려줌

print(m)

"""

"""

m = p.match('python')
print(m.group())
#python 이 나옴

print(m.start())
#0 첫시작 스타트의 인덱스 0

print(m.end())
#6 마지막 끝자리 인덱스 6

print(m.span())
#(0, 6) 튜플형태로 리턴

"""


