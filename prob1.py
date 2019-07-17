n = int(input("number of students:"))

b = map(int, input().split())
v = list(set(b))
v.remove(max(v))
print(max(v))



