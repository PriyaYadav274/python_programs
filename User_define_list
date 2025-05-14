# WAP to create a user define list & perform the following operations.
# 1-) count total numbers of element in the list.
# 2-) reverse the elments of the list.
# 3-) delete a particular element from the list. (given by the user)

n = int(input("How many numbers you want to enter: "))
list1 = []
i = 1
while i<=n:
    el = input("Enter element: ")
    list1.append(el)
    i+=1
print(list1)
print("Select an option")
print("Press 1 to count total numbers of element in the list")
print("Press 2 to reverse the element of the list")
print("Press 3 to delete a particular element from the list")
choice = int(input("Enter your choice: "))
if choice ==1:
    print(len(list1))
elif choice ==2:
    list1.reverse()
    print(list1)
elif choice ==3:
    d = input("Enter element that you want to delete from the list: ")
    list1.remove(d)
    print(list1)
else:
    print("invalid value")

