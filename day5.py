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

student_scores = input("Input a list of students scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"the hightes score in the class is: {max_score}")    