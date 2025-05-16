# WAP to create a user define set object and perform these.
# 1- remove an existing element from the set.
# 2- create another set object and after that check whether it's a subset of first set object or not.
print("To create a set enter elements.")
n = int(input("How many elements you want to enter: "))
s1=set()
for i in range(0,n):
    e = int(input("Enter elements: "))
    s1.add(e)
print(s1)
print("Press 1 to remove an existing elements form the set")
print("Press 2 to create another set object and after that check it is a subset of 1st set object or not")
choice = int(input("Enter choice between (1-2): "))
if choice == 1 :
    r = int(input("Enter elements that you want to remove: "))
    s1.remove(r)
    print(s1)
elif choice == 2:
    n = int(input("How many elements you want to enter for second set: "))
    s2 = set()
    for i in range(0,n):
        el = int(input("Enter elements: "))
        s2.add(el)
    print(s2)
    if s2.issubset(s1):
        print("Its a subset of set 1")
    else:
        print("Its not a subset of set 1")
else:
    print("Invalid value, try again")
