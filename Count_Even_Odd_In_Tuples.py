#Counting Even and Odd Elements in User-Created Tuples
l = []
n = int(input("How many tuple you want to create: "))
for i in range(1,n+1):
    t = []
    nt = int(input(f"How many elements you want to enter in {i} tuple: "))
    for j in range(0,nt):
        e = int(input("Enter elements: "))
        t.append(e)
    a = tuple(t)
    l.append(a)
print(l)
even = []
odd = []
for k in l:
    for m in k:
        if(m%2==0):
            even.append(m)
        else:
            odd.append(m)
print("Even: ",len(even))
print("Odd: ",len(odd))
