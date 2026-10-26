
# Advanced Numeric Pattern Generator

print("1. Hollow Diamond")
print("2. Symmetric Number Pyramid")

choice = int(input("Choose a pattern (1 or 2): "))
n = int(input("Enter the number of rows (minimum 1): "))

if n < 1:
    print("Invalid dimension! Enter a number greater than 0.")

elif choice == 1:
    # Hollow diamond
    for i in range(1, n + 1):
        spaces = n - i
        print(" " * spaces, end="")

        if i == 1:
            print("1")
        else:
            print("1" + " " * (2 * i - 3) + str(i))

    for i in range(n - 1, 0, -1):
        spaces = n - i
        print(" " * spaces, end="")

        if i == 1:
            print("1")
        else:
            print("1" + " " * (2 * i - 3) + str(i))

elif choice == 2:
    # Symmetric number pyramid
    for i in range(1, n + 1):
        print(" " * (n - i), end="")

        for j in range(1, i + 1):
            print(j, end="")

        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()

else:
    print("Invalid choice! Select 1 or 2.")
