import re

data = """
park 800905-1049118
kim 700905-1059119
"""

#주민등록번호의 뒷자리를 * 문자로 변경하시오 (정규표현식 미사용)

"""
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
"""

#주민등록번호의 뒷자리를 * 문자로 변경하시오 (정규표현식 사용)

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
