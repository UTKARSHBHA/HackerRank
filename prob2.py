N = int(input("no. of students:"))

b = []
for i in range(N):
    name = input("name:")
    score = float(input("score:"))
    a = [name, score]
    b.append(a)

b.sort(key = lambda v : v[1])


c = []
print(b)
for x in range(1, len(b)-1):
    if b[0][1] == b[x][1]:

        if b[x+1][1] == b[x+2][1]:
            c.append(b[x+2][0])
            c.sort()


        elif b[x+1][1] != b[x+2][1]:
            c.append(b[x+1][0])


    elif b[0][1] != b[x][1]:

        if b[1][1] == b[x][1]:
            c.append(b[x][0])
            c.sort()



        elif b[1][1] != b[2][1]:
            c.append(b[1][0])

print(c)
for i in c:
    print(i)