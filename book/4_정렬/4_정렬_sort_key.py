"""
 - 정렬 - 라이브러리 (sorted, sort)

*key값을 매개변수로 받아서 sorted or sort 함수 사용하기
*lambda로도 사용 가능
"""

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

result = sorted(array, key=lambda data: data[1])
print(result)
