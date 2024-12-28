 # MonthNames.py
# month_number = int(input("Enter the month: "))
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# if 1 <= month_number <= 12:
#     print(f"Month {month_number} is {months[month_number - 1]}")
# else:
#     print("Invalid month number.")
 ###########################################################################################################
# # Cinema Ticket Pricing
# age = int(input("Enter your age: "))
# if age < 16:
#     ticket_price = 6 / 2  # Half price
# elif age >= 60:
#     ticket_price = 6 / 3  # Third of the price
# else:
#     ticket_price = 6  # Full price
#
# print(f"Your ticket costs £{ticket_price:.2f}")
#################################################################################################3
# BodyMassIndex.py
# weight = float(input("Enter your weight in (kg): "))
# height = float(input("Enter your height in (m): "))
#
# # Calculate BMI
# bmi = weight / (height ** 2)
# print(f"Your BMI is: {bmi:.2f}")
#
# # Check weight status
# if bmi < 18.5:
#     status = "underweight"
# elif 18.5 <= bmi <= 24.9:
#     status = "normal"
# elif 25 <= bmi <= 29.9:
#     status = "overweight"
# else:
#     status = "obese"
#
# print(f"You are in the '{status}' range.")
######################################################################################
# Greatest Among 3 Numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# greatest = max(num1, num2, num3)
# print(f"The greatest number is: {greatest}")
###############################################################################
# Factorial of a Given Number
# Factorial of a Given Number
# number = int(input("Enter a number: "))
# factorial = 1
#
# for i in range(1, number + 1):
#     factorial *= i
#
# print(f"The factorial of {number} is {factorial}")

###################################################################################
# # Reverse a Number using while loop
# number = int(input("Enter a number: "))
# reversed_number = 0
#
# while number > 0:
#     reversed_number = reversed_number * 10 + number % 10
#     number //= 10
#
# print(f"The reversed number is: {reversed_number}")
#############################################################################################
#  Finding the Multiples of a Number
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")
#################################################################################################
# Print Inputted Value and Break on 'done'
# while True:
#     user_input = input()
#     if user_input == 'done':
#         print("Done")
#         break
#     print(user_input)
####################################################################################################
# FizzBuzz Program
# for i in range(1, 11):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
###################################################################################################
# Print Pattern
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()