# # day2 "Data Types"

# # "strings"
# print("Hello"[4])

# #Integer
# print(12 + 12)

# #Float
# print(1.1 + 1.1)

# #Boolean Type
# True
# False

#vid-19

#type checking

# print(type("123"))
# num_char = len(input("What is your name?"))
# # converted int into string data type by using name of data
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters." )

#vid-20 Challenge

# two_digit_num = str(input("Enter the two digit number\n"))

# # print(type(two_digit_num))

# sum = int(two_digit_num[0]) + int(two_digit_num[1])
# print(sum)

#video 21 **** Math Formulas ****
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 2 #power formula
# P    E     M     D     A    S
#()   **     *    /     +     -

#print(3 * 3 + 3 / 3 - 3)

#vide - 22 "Challenge"

#BMI = weight / height square

# weight = input("Enter your weight in kg:\n")
# height = input ("Enter your height in m:\n")
# BMI = int(weight) / float(height) ** 2
# bmi_as_int = BMI
# print(bmi_as_int)

#video-23      *** Math functions***
# import math
# result = math.floor(BMI)
# print(result)
# print(round(2.666666, 2))
# print(8 // 3)
# print(8 / 3)
# score = 0
# score /= 2
# score += 1
# # convert multiple data type at once us f-string
# print(f"your score is {score}, ")

#video - 24 "challenge"
# age = input("What is your current age?")

# living_years = 90 - int(age)

# x_days = (living_years) * 365
# y_weeks = (living_years) * 52
# z_month = (living_years) * 12

# message = (f"you have {x_days} days, {y_weeks} weeks, and {z_month} months left")
# print(message)

#video-25 " day-2 final challenge"
 
print("Welcome to the tip calculator")

total_bill = float(input("What was the tital bill?"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_persons = int(input("How many people to split the bill?"))

bill_plus_tip = total_bill * tip_percentage / 100 + total_bill
split_bill = bill_plus_tip / number_of_persons
# final_amount = round(split_bill, 2)
final_amount = "{:.2f}".format(split_bill) # formula for using adding values after point in math
final_bill = (f"Each person should pay: ${final_amount}")

print(final_bill)