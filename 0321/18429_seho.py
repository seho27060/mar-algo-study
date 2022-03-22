def find_(get_):
    if lst[get_-1] == 0:
        return find(get_//2)*find_(get_-get_//2)
    else:
        return lst[get_-1]

a,b,c = map(int,input().split())
lst = [0]*b
lst[0] = a
result =find_(b)
print(result%c)
