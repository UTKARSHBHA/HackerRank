n = int(input("number of students:"))



b = input("score:")
A = b.split(" ")
print(A)
A = [int(o) for o in A]
A.sort(reverse = True)


print(A)

if A[0] != A[1]:
    print(A[1])
else:
    for x in range(1, n+1):
        if A[0] != A[x]:
            print(A[x])
            break





