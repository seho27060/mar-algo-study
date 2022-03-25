tc_num = int(input())

for tc in range(tc_num):
    n, n_hex = input().split()
    n_hex = list(n_hex)

    for idx in range(int(n)):
        if ord(n_hex[idx]) >= 65:
            n_hex[idx] = bin(ord(n_hex[idx]) - 55)
        else:
            n_hex[idx] = bin(int(n_hex[idx]))

    for idx in range(int(n)):
        get_ = n_hex[idx][2:]
        for _ in range(abs(len(get_)-4)):
            get_ = "0"+get_
        n_hex[idx] = get_
    print("#{0} {1}".format(tc+1,"".join(n_hex)))
    ## A 는 10, ord("A")-55, F는 15, 10은 16(16^1+0*16^0)
