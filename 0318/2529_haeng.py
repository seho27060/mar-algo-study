N= int(input())
Nlist=list(input().split())

num=[0,1,2,3,4,5,6,7,8,9]


ST = []
result = []

def find(x):
    if x==N+1:
        Y=''
        for i in ST:
            Y += str(i)
        result.append(Y)
        return

    for i in num:
        if i in ST:
            continue
        if Nlist[x-1] == '>' and ST[-1]>i:
            ST.append(i)
            find(x + 1)
            ST.pop()
        elif Nlist[x-1] == '<' and ST[-1]<i:
            ST.append(i)
            find(x+1)
            ST.pop()

for i in num:
    ST.append(i)
    find(1)
    ST.pop()

print(max(result))
print(min(result))
