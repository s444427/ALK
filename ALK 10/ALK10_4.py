n = int(input("n: "))
r = int(input("rank: "))

tab = []

for i in range(0, n-2):
    x = r % n
    r = r // n
    tab.append(x)

tab2 = []
for i in range(0, len(tab)):
    x = int(len(tab)-i-1)
    tab2.append(tab[x])

for i in range(0, len(tab2)):
    tab2[i] += 1

print("kod prufera: ")
print(tab2)
