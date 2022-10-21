"""
20221021

- 가장 큰 수
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42746
    
주의할점
  - 아이디어는 근접하게 풀이했지만, 예외 케이스를 생각해내기 어려웠음
  - 1,000이하의 수 이므로, 첫번째 자리수로 3자리 수를 맞추도록 padding 하려했으나,
  - 아래 예외케이스가 존재
    - [979, 97, 978, 81, 818, 817] -> 9799797881881817
    - 여기서 81과 818은 결국 818,818로 어떻게 정렬될지 알 수 없음
    - 결과적으로 818 -> 81 순으로 가야 81881 > 81818 이므로 문자열의 길이도 신경써야함
  - 따라서 3자리로만 맞춰주는게 아니라 *3으로 기존 문자열도 보존하면서 자리수를 맞춰주는 것이 필요함
  - 또한 모두 0일 경우를 대비하여 마지막에 int로 한번 변환해주는 포인트도 놓치지말자 

*Referece
https://school.programmers.co.kr/learn/courses/30/lessons/42746/solution_groups?language=python3

"""
ls_ = [979, 97, 978, 81, 818, 817]

# 1. 답안
def solution(numbers):
    # 예외 케이스를 고려하지 못하는 원래 내 답안
    #n_ls = sorted(map(str,numbers),key=lambda x : x.ljust(3,x[0]), reverse=True)
    
    # Reference
    n_ls = sorted(map(str,numbers),key=lambda x : x*3, reverse=True)
    return str(int("".join(n_ls)))