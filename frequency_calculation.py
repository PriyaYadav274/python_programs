l = []
l2 = []
c = []
print("||Enter elements to check frequency of each elements||\n")
n = int(input("How many elements you want to enter: "))
for i in range(0,n):
    el = int(input("Enter elements: "))
    l.append(el)
for i in l:
    if (i in l2):
        i+=1
    else:
        l2.append(i)
for j in l2:
    a = l.count(j)
    c.append(a)
print("\nElement : Frequency")
for e,f in zip(l2,c):
    print(e, ":" ,f)
