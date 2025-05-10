print("||Show numbers with their cube value in a tuple.||\n")
n = int(input("How many tupels you want to create: "))
l = []
for i in range(0,n):
    e = int(input("Enter number for their corresponding cube value: "))
    t = [e,e**3]
    l.append(tuple(t))
print("(Number, Cube)")
for j in l:
    print(j)
