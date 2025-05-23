# WAP to create user_define dict object

user_info = {}
n = int(input("How many elements you want to enter: "))
for i in range(0,n):
    k =input("Enter key values: ")
    d =input("Enter data values: ")
    user_info[k]=d
print(user_info)
