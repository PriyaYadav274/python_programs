# WAP to create a user define string and perform the following operation.
# 1-)check it contains vowels or not.
# 2-) print data in upper case & lower case.
print("||Create a string check whether the string contains vowels or not also print")
print("data in upper case & lower case.||\n")
s1 = input("Enter string: ")
print("\nSelect option by pressing the number between(1-2)\n")
print("Press 1 to check whether the string contains vowels or not")
print("Press 2 to convert the string in lower and upper case\n")
choice = int(input("Enter choice: "))
if choice ==1:
    if 'a' in s1:
        print("String contains vowels")
    elif 'e' in s1:
        print("String contains vowels")
    elif 'i' in s1:
        print("String contains vowels")
    elif 'o' in s1:
        print("String contains vowels")
    elif 'u' in s1:
        print("String contains vowels")
    else:
        print("String doesn't contains vowels")  
elif choice ==2:
    print("Lower Case: ",s1.lower())
    print("Upper Case: ",s1.upper())
else:
    print("invalid value")
    
