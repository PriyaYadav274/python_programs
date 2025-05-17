# WAP to create 2 user define set object and print non unique elements.
print("To print non-unique elements.\n")
n = int(input("How many elements you want to enter for set 1: "))
s1 = set()
for i in range(1,n+1):
    e = int(input(f"Enter {i} elements: "))
    s1.add(e)

n = int(input("How many elements you want to enter for set 2: "))
s2 = set()
for i in range(1,n+1):
    e = int(input(f"Enter {i} elements: "))
    s2.add(e)


s3 = set(s1.union(s2))
s4 = set(s1.intersection(s2))
print()
print("set 1",s1)
print("set2",s2)
print("non unique elements : ",s3-s4)
