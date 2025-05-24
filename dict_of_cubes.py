# Program to create a user-defined dictionary
# where the value is the cube of the key

# Initialize an empty dictionary
d = {}

# Ask user how many elements they want to enter
n = int(input("How many elements you want to enter: "))

# Loop to get key input and compute cube as value
for i in range(n):
    k = int(input("Enter key value (integer): "))
    d[k] = k ** 3  # Store cube of key as value

# Print the final dictionary
print("Resulting dictionary:", d)
