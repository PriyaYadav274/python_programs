# WAP to take a percentage of a student and check which grade he/she belongs.
# 90-100 (Grade A)
# 80-90 (Grade B)
# 70-80 (Grade C)
# 60-70 (Grade D)
# 50-60 (Grade E)
# n <50 (Grade F)

n = int(input("Enter your percentage: "))
if(n>90 and n<=100):
    print("Grade A")
elif(n>80 and n<=90):
    print("Grade B")
elif(n>70 and n<=80):
    print("Grade C")
elif(n>60 and n<=70):
    print("Grade D")
elif(n>50 and n<=60):
    print("Grade E")
elif(n<=50):
    print("Grade F")
else:
    print("invalid value, recheck!")
