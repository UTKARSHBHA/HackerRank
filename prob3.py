n = int(input("no. of students"))

subjects = ["maths", "physics", "chemistry"]
marks = []
name = []
dicf = {}
for i in range(n):
    d = input("name").split()

    name.append(d[0])
    for y in range(1, 4):
        marks.append(float(d[y]))

    dic = dict(zip(subjects, marks))

    print(dic)
    dicf[name[i]] = dic
    marks.clear()

print(dicf)
nm = input("st_nm")
def avg(h):
    sc = dicf[h].values()
    print(list(sc))
    tt = 0
    for b in sc:
        tt +=  b
        vb = tt/3
    return "%.2f" % vb
print(avg(nm))

