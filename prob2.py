n = int(input("no. of students"))


nested = []
names = []
scores = []
for i in range(n):
    nm = input("name")
    names.append(nm)
    sc = float(input("score"))
    scores.append(sc)
    nested.append([nm, sc])

st = list(set(scores))
st.sort()

mnsc = st[1]

final = []

for i in range(n):
    if nested[i][1] == mnsc:
        final.append(nested[i][0])

final.sort()
for i in final:
    print(i)
