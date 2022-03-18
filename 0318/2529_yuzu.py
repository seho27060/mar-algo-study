k = int(input())
a = list(input().split())
lst = ''
rev_lst = ''
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
rev_num = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
for i in range(k):
    cnt = 0
    if a[i] == '>':
        cnt += 1
        while k>i+cnt and a[i+cnt] == '>':
            cnt += 1
        lst += num.pop(cnt)
    else:
        lst += num.pop(0)
for i in range(k):
    cnt = 0
    if a[i] == '<':
        cnt += 1
        while k>i+cnt and a[i+cnt] == '<':
            cnt += 1
        rev_lst += rev_num.pop(cnt)
    else:
        rev_lst += rev_num.pop(0)
lst += num.pop(0)
rev_lst += rev_num.pop(0)
print(rev_lst)
print(lst)