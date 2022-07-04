"""
20220704 소트인사이드

- No.: 1316
- type: 구현, 문자열
- Problem : 그룹단어 체크하기

*나올수있는 조건을 좀 더 생각하고 구현하기

ex)
input:
    3
    happy
    new
    year
output: 
    3

"""

# solve 1
N=int(input())
cnt=0
for i in range(N):
    str_ = input()
    bl_ = True
    for j in range(len(str_)):
        a = ['1' if i==list(str_)[j] else '0' for i in list(str_)[j+1:]]
        if '01' in ''.join(a):
            bl_=False
    if bl_:
        cnt+=1
print(cnt)


# reference
N=int(input())
cnt=0
for i in range(N):
    word = input()  
    bl_=True
    for j in range(len(word)-1):
        if word[j]!=word[j+1]:
            if word[j] in word[j+1:]:
                bl_=False
                break
    if bl_:
        cnt+=1
print(cnt)



