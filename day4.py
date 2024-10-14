##video-40 " Randomization"
import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_flaot = random.random()
# print(random_flaot)

## video - 41 "challenge flip the coin"
# guess = random.randint(0, 1)
# if guess == 0:
#     print(f"Tails {guess}")
# else:
#     print(f"Heads {guess}")

##video - 42  "List Data Structure"

# states_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
#                 "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
#                 "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
#                 "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
#                 "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
#                 "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
#                 "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
#                 "Wisconsin", "Wyoming"]
 

# print(states_names[5])

# states_names.append("future state")
# print(states_names)

# video - 43 "challenge"

# name_string = input("Give me the names, seperated by comma. ")
# names = name_string.split(", ")
# num_item_length = len(names)
# randdom_name = random.randint(0, num_item_length - 1)

# print(f"{names[randdom_name]} will pay the bill")

# "use choice() function to do directly above challenge"

# random_choice = random.choice(names)
# print(f"{random.choice(names)} will pay the bill!")

#video - 44 "IndexError and nesting list"
# fruits = ["apple", "bannna", "mango"]
# veges = ["tomato", "potato", "celery"]
# mix = [fruits, veges]
# print(mix)

#video - 45 " challenge"
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where you want to put your treasure?")
horizontal = int(position[0])
vertical = int(position[1])
# print(horizontal)
# print(vertical)
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")