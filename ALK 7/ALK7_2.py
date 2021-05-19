# Input list
N = [-1]
X = input("f: ").split()
for i in X:
    N.append(int(i))

n = len(N)-1

final = []
sub = []

for q in range(1, n + 1):
    # print("section: ", q)
    for i in range(1, n + 1):
        if N[i] == q:
            sub.append(i)
            # print("sub append: ", i)
    if sub != []:
        final.append(sub)
    sub = []

print(final)
