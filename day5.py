#video - 48 -49 "Loops"
#for in loop

# names = ["usman", "ali", "adil"]
# for name in names:
#     print(name)

#video -50 " challenge - Average Height Exercise"

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# #     print(student_heights)
# print(student_heights)
# total_sum = 0
# count = 0
# for num in student_heights:
#     total_sum += num
#     count += 1
# average = round(total_sum/count)
# print(average)

#video-51 "coding challenge - Highest Score Exercise"

# student_scores = input("Input a list of students scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# max_score = student_scores[0]
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"the hightes score in the class is: {max_score}")    

# video - 52 " Range function"

# for number in range(1, 11): # last digit is not included in the range
#     print(number)
# for number in range(1, 11, 2): # put gap of 2 in range
#     print(number)
# total_sum = 0    
# for number in range(1, 101):
#     total_sum += number
# print(total_sum)

#video - 53 " challenge of range"

# even_sum = 0
# for even_number in range(2, 101, 2):
#     #if even_number % 2 == 0:
#         even_sum += even_number
# print(even_sum)

#video - 54 " challenge"

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzBuzz")
#     elif number % 5 == 0:
#         print("buzz")
#     elif number % 3 == 0:
#         print("fizz")
#     else:
#         print(number)

# video - 55 "final challenge password generator"
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
        
        