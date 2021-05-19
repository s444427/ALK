def PodzialRGF(n, k, B):
    F = []
    for i in range(0, n + 1):
        F.append(0)

    for i in range (0, k+1):
        for j in B[i]:
            F[j] = i

    return F


n = []
print("Podaj podzbiory w postaci '{x, y}{z}' tzn. rozdzielając podzbiory nawiasami klamrowymi, a elementy podzbiorów przecinkiem")
n = input().split("{")

# Clear input
y = ''
sub = []
sub2 = []
n2 = []

for i in n:
    if i != "":
        x = i
        coma = 0
        sub = []
        sub2 = []

        for z in x:
            if ord(z) in range(48, 58) or ord(z) == 44:
                if ord(z) == 44:
                    coma = 1
                y = y + z
        if coma == 1:
            sub = y.split(',')
            n2.append(sub)
        else:
            sub.append(y)
            n2.append(sub)
        y = ''


# Count elements
countn = 0
countk = 0
n = [[-1]]
for i in n2:
    c = [int(x) for x in i]
    n.append(c)

    countk += 1
    for j in i:
        countn += 1

# print(n)
# print(n2)
# print(countn,countk)

# RGF
final = []
final = PodzialRGF(countn, countk, n)
final.pop(0)
print(final)
