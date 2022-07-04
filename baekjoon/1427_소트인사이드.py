"""
20220704 소트인사이드

- No.: 1427
- type: 정렬, 문자열
- Problem : 숫자정렬하기

*문자열을 바로 list화해서 쪼개기가 가능함

ex)
input : 61423
output : 64321

"""

N=input()
print(int(''.join(sorted(N,reverse=True))))
