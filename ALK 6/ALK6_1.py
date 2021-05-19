n = int(input("j: "))

# Numer następnego bloku dla bloku i
N = [-1]
for i in range(0, n):
    N.append(0)
N = [int(x) for x in N]

# Numer poprzedniego bloku dla bloku i
P = [-1]
for i in range(0, n):
    P.append(0)
P = [int(x) for x in P]

# Numer bloku zawierającego i
B = [-1]
for i in range(0, n):
    B.append(1)
B = [int(x) for x in B]

# Kierunek poruszania się
PR = [-1]
for i in range(0, n):
    PR.append(True)
PR = [int(x) for x in PR]

# Lista końcowa iteracji
final = []
sub = []
for i in range(1, n + 1):
    sub.append(i)
final.append(sub)
print(final)
final = []
sub = []
# print("final: ", final)

# ##################
prevfinal = []
j = n
j = int(j)

while j > 1:
# for z in range(0, 7):

    # print('N:', N)
    # print('P: ', P)
    # print('B: ', B)
    # print('PR: ', PR)
    # print("")

    k = B[j]
    # # print('k', k)
    # # print("")

    if PR[j] == True:
        if N[k] == 0:
            # print("N[k]==0")
            N[k] = j
            N[j] = 0
            P[j] = k
            B[j] = j

        elif N[k] < j:
            # print("N[k] < j")
            B[j] = N[k]

        elif N[k] > j:
            # print("N[k] > j")
            P[j] = k
            N[j] = N[k]
            P[N[k]] = j
            N[k] = j
            B[j] = j
    elif PR[j] == False:
        B[j] = P[k]
        if j == k and N[k] == 0:
            N[P[k]] = 0
        elif j == k and N[k] != 0:
            N[P[k]] = N[k]
            P[N[k]] = P[k]

    j = n
    while (j > 1) and ((PR[j] and B[j] == j) or (not PR[j] and B[j] == 1)):
        PR[j] = not PR[j]
        j = j - 1

    # print("final", final)
    for q in range(1, n + 1):
        # print("section: ", q)
        for i in range(1, n + 1):
            if B[i] == q:
                sub.append(i)
                # print("sub append: ", i)
        if sub != []:
            final.append(sub)
        sub = []
    if final != prevfinal:
        print(final)
    prevfinal = final
    # print('final', final)
    # # print('sub', sub)
    final = []
