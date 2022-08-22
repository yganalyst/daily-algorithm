"""
20220701 done

- No.: 2439
- type: 구현
- Problem : 문자열 padding 문제

*문자열로 채울수도 있긴하지만, padding 함수 쓰기
* rjust (우정렬), ljust (좌정렬)

"""

T_n = int(input())
star = "*"
for i in range(T_n):
    print(star.rjust(T_n-i,' ').ljust(T_n,star))
