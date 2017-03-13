params = raw_input()
m,n,k = map(int, params.split(' '))

result = []
for j in range(k):
    l = raw_input()
    l = map(int, l.split(' '))

    max = 0
    sub = []
    ok = True

    for index, i in enumerate(l):
        if i - index > m:
            ok = False
            break
        if i > max:
            max = i
            if sub:
                if sorted(sub, reverse=True) != sub:
                    ok = False
                    break
            sub = []
            continue
        else:
            sub.append(i)
    else:
        if sub:
            if sorted(sub, reverse=True) != sub:
                ok = False

    if ok:
        result.append("YES")
    else:
        result.append("NO")

for res in result:
    print(res)
