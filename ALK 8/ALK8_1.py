n = int(input("n: "))
p = []
p = input("p: ").split(',')
p = [int(x) for x in p]
p.insert(0, -1)


i = n-1
while p[i] > p[i+1]:
    i -= 1

if i != 0:
    j = n
    while p[j] < p[i]:
        j -= 1

    p[j], p[i] = p[i], p[j]

    q = []
    for i in range(1, i+1):
        q.append(p[i])

    for i in range(n, i, -1):
        q.append(p[i])
    print('następnik: ', q)
else:
    print('brak następnika')
