N,K = map(int,input().split())
Nlist=[]
for i in range(N):
    a,b,c,d = input().split()
    Nlist.append([int(a),int(b)*(1000000**6)+int(c)*(1000000**3)+int(d)*1000000])

ranking=[[] for i in range(N+1)]
ranking[0] = '@'

rank=1
ST=[]
while Nlist:
    higher=0
    for i in range(len(Nlist)):
        if Nlist[i][1] > higher:
            higher = Nlist[i][1]


    for i in reversed(range(len(Nlist))):
        if Nlist[i][1] == higher:
            ranking[rank].append(Nlist.pop(i))
    rank += len(ranking[rank])

for j in range(1,N+1):
    for k in ranking[j]:
        if k[0] == K:
            print(j)
