## Conditional Statements if/else if/elif/else
##video-29
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120:
	print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

##video-30
print("Even Odd function checking")
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("Its Even number")
else:
    print("Its Odd number")

##video-32 "Challenge"
height = float(input("Entter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)
bmi = 18
if bmi > 35:
    print(f"Your bmi is {bmi}, and you are clinically obse")
elif bmi > 30:
    print(f"Your bmi is {bmi}, and you are Obese")
elif bmi > 25:
    print(f"Your bmi is {bmi}, and you are Overweight") 
elif bmi > 18.5:
    print(f"Your bmi is {bmi}, and you are normal weight")
else:
    print(f"Your bmi is {bmi}, and you are underweight")

#video-32 "Challenge"

print("leap year challeng")

year = int(input("Enter the year: "))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(f"{year} it's leap year")
		else:
			print(f"{year} its Not a leap year")
	else:
		print(f"{year} its a leap year")
else:
	print(f"{year} its Not a leap year")

#vid-33 "Final Challenge"

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if choice1 == "left":
    choice2 = input("you come to a lake. There is a an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "blue":
            print("game over")
        elif choice3 == "red":
            print("game over")
        else:
            print("that color is not available plz choose write color else fuck off!") 
    else:
        print("game over")
else:
    print("game over")
