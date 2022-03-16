# n마리 소중 m마리 선별, 총 몸무게 합이 소수가 되는 경우 출력.
# 오름차순 출력, 없다면 -1
# 1 <= m <= n <= 9
# 1 <= 몸무게 <= 1000
# 1000*3 까지 소수 카운팅?..

prime_lst = []

for i in range(2,3001):
    check = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            check = False
            break
    if check:
        prime_lst.append(i)

def find_prime_cows(lst,nums):
    if len(lst) == m:
        get_sum = 0
        for get_ in lst:
            get_sum += cows[get_]
        if get_sum in prime_lst and get_sum not in result:
            result.append(get_sum)
    else:
        for nxt in range(len(nums)):
            lst2 = lst.copy()
            nums2 = nums[nxt+1:].copy()
            lst2.append(nums[nxt])
            find_prime_cows(lst2,nums2)

n,m = map(int,input().split())
cows = list(map(int,input().split()))
cow_num = [i for i in range(len(cows))]
result = []

find_prime_cows([],cow_num)
if result:
    print(" ".join(map(str,sorted(result))))
else:
    print(-1)