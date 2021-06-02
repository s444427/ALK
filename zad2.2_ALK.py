n = 0
r = 0
sublist = []

n = int(input("Podaj n: "))

# get r
r = int(input("Podaj r: "))
endbinary = bin(r)[2:]

while len(endbinary) < n:
    endbinary = "0" + endbinary

for i in range(0, n):
    if endbinary[i] == '1':
        sublist.append(i + 1)

print("Ciąg o danym indeksie to: ")
print(sublist)
