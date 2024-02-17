# task 1 & 2:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

greatest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print(f"The greatest number is {greatest}")
print(f"The smallest number is {smallest}")

# task 3:
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two numbers are equal and the largest is", greatest)
