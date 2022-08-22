"""
 - 기출: 문자열 재정렬
 - type : 구현
 - problem : 
     알파벳 대문자와 숫자(0~9)로 이루어진 문자열이 주어질때,
     모든 알파벳을 오름차순정렬하고, 뒤의 숫자는 합으로 출력
     ex) K1KA5CB7 -> ABCKK13

*알파벳과 숫자를 분리해야함
*알파벳은 정렬하고, 숫자는 합쳐야함

*알파벳 식별을 위해 isalpha 나 ord(아스키 코드값)를 활용할 수 있음
* ref
 - https://velog.io/@byukbyak/Python%EC%9D%B4%EC%BD%94%ED%85%8C-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%AC%EC%A0%95%EB%A0%AC
 - https://unie2.tistory.com/112
"""


s = sorted(input())
num_list=list(map(str,range(10)))

cut=0
for i in range(len(s)):
    if s[i] not in num_list:
        cut=i
        break

print(''.join(s[cut:])+str(sum(map(int,s[:cut]))))