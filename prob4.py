n = int(input("no of students read english np"))

eng = set(input("roll no").split())


b = int(input("no of students read french np"))

frn = set(input("roll no").split())

total = eng.union(frn)
print(len(total))