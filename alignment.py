f = open("input", "r")
o = open("output", "w")
p = list(f.readline().strip())
s = list(f.read().replace("\t","").replace("\n", "").replace("\r", "").strip())
b = open("BLOSUM62.txt", "r")
letters = b.readline().replace("\t","").replace("\n", "").replace("\r", "").strip().split()
mat = []
for _ in range(0,len(letters)):
            line = b.readline().replace("\t","").replace("\n", "").replace("\r", "").strip().split()
            mat.append([int(line[i]) for i in range(1, len(line))])
dist = []
path = {}
for i in range(0, len(p) + 1):
    row = [] 
    for j in range(0, len(s) + 1):
        row.append(0)
    dist.append(row)
def matrix(i, k):
    return mat[letters.index(i)][letters.index(k)]
for i in range(0,len(p)):
    dist[i + 1][0] = dist[i][0] - 5
    path[(i + 1, 0)] = (i, 0)

for j in range(0,len(s)):
    dist[0][j + 1] = dist[0][j] - 5
    path[(0, j + 1)] = (0, j)

for i in range(0,len(p)):
        for j in range(0,len(s)):
            pmis = matrix(p[i],s[j])
            dist[i + 1][j + 1] = max(dist[i][j] + pmis , dist[i][j + 1] - 5 , dist[i + 1][j] - 5)
            if dist[i + 1][j + 1] == dist[i][j] + pmis:
                path[(i + 1, j + 1)] = (i, j)
            elif dist[i + 1][j + 1] == dist[i][j + 1] - 5:
                path[(i + 1, j + 1)] = (i, j + 1)
            elif dist[i + 1][j + 1] == dist[i + 1][j] - 5:
                path[(i + 1, j + 1)] = (i + 1, j)

score = dist[len(p)][len(s)]
print(dist)
out1 = ''
out2 = ''
i = len(p) - 1
j = len(s) - 1
while i >= 0 or j >= 0:
    print(i)
    print(j)
    if i >= 0 and path[(i + 1, j + 1)] == (i, j +1 ):
        out1 = p[i] + out1
        out2 = '-' + out2
        i -= 1
    elif j >= 0 and path[(i + 1, j + 1)] == (i + 1, j):
        out1 = '-' + out1
        out2 = s[j] + out2
        j -= 1
    else:
        out1 = p[i] + out1
        out2 = s[j] + out2
        i -= 1
        j -= 1
print(dist[-1][-1])
print(out1)
print(out2)
o.write(str(score))
o.write("\n")
o.write("".join(out1))
o.write("\n")
o.write("".join(out2))