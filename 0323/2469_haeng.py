ABC=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k=int(input())
n=int(input())
want=input()
nlist=[]
for i in range(n):
    A=input()
    if A == '?'*(k-1):
        idx=i
    nlist.append(A)

ST=[]
ST2=[]
for i in range(k):
    if i == k-1:
        ST.append(ABC[i])
        ST2.append(want[i])
    else:
        ST.append(ABC[i])
        ST2.append(want[i])
        ST.append('*')
        ST2.append('*')


for i in range(idx):
    for j in range(k - 1):
        if nlist[i][j] == '-':
            ST[j*2], ST[j*2+2] = ST[j*2+2], ST[j*2]
for i in reversed(range(idx+1,n)):
    for j in range(k - 1):
        if nlist[i][j] == '-':
            ST2[j*2], ST2[j*2+2] = ST2[j*2+2], ST2[j*2]

result=''
for i in range(0,k+k-3,2):
    if ST[i]==ST2[i] and ST[i+2]==ST2[i+2]:
        result += '*'
    elif ST[i] == ST2[i+2] and ST[i+2] == ST2[i]:
        result += '-'
    else:
        result += '*'


for j in range(k - 1):
    if result[j] == '-':
        ST[j*2], ST[j*2+2] = ST[j*2+2], ST[j*2]

if ST == ST2:
    print(result)
else:
    print('x'*(k-1))