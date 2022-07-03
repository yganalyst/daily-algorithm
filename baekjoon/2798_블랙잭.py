"""
20220703 블랙잭

- No.: 2798
- type: brute force
- Problem : 세개 숫자의 합을 제한값 내에서 최대화

*완전탐색이긴 하지만 복잡도를 줄이는 방향

"""

# solve 1
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum = 0
for x in num_list:
    for y in num_list:
        for z in num_list:
            if (x==y)|(y==z)|(x==z):
                continue
            ch_ = x+y+z
            if (max_sum < ch_) & (M >= ch_):
                max_sum = ch_
print(max_sum)

# solve 2 (개선)
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum = 0
for x in range(N):
    for y in range(x+1,N):
        for z in range(y+1,N):
            ch_ = num_list[x]+num_list[y]+num_list[z]
            if (max_sum < ch_) & (M >= ch_):
                max_sum = ch_
print(max_sum)
