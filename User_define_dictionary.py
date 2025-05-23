# WAP to create user_define dict object

dict = {}
n = int(input("How many elements you want to enter: "))
for i in range(0,n):
    k =input("Enter key values: ")
    d =input("Enter data values: ")
    dict[k]=d
print(dict)
