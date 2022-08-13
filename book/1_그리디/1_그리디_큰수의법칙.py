"""
 - 큰 수의 법칙
 - type : 그리디
 - problem : 
     숫자 N개를 M번 더하여 가장 큰 수를 만들기(중복가능)
     단, 하나의 수를 K번 까지만 연속 중복 가능
     ex) 2,4,5,4,6 (M,K=8,3) : 6+6+6+5+6+6+6+5
         3,4,3,4,3 (M,K=7,2) : 4+4+4+4+4+4+4

*나누어떨어져 버리는 경우(8/4=2) 주의!
*M개 중 수열(그룹)이 몇개? -> 그럼 큰 수가 몇개?
*ex) 6 6 6 6 5 6 6 6  (수열 1개, 나머지 3개)

"""

N,M,K = map(int,input().split(" "))
ls_ = sorted(map(int,input().split(" ")), reverse=True)
first_cnt = M//(K+1)*K + M%(K+1)
second_cnt = M-first_cnt
print(ls_[0]*first_cnt+ls_[1]*second_cnt)