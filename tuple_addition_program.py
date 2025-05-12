print("||Enter equal numbers of element for both the tuples||")
n = int(input("\nHow many elements you want to enter for first tuple: "))
t1 = []
for i in range(0,n):
    x = int(input("Enter elements: "))
    t1.append(x)
print("\ntuple 1:",tuple(t1))

n = int(input("How many elements you want to enter for second tuple: "))
t2 = []
for i in range(0,n):
    x = int(input("Enter elements: "))
    t2.append(x)
print("\ntuple 2:",tuple(t2))


r = []
for i in range(0,n):
    r.append(t1[i] + t2[i])
print("\nAddition of tuple 1 and tuple 2 : ",tuple(r))
