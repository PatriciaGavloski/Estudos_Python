"""height = 1.65
weight = 84

bmi = weight / (height)**2

print(bmi)

print(round(bmi))

print(round(bmi, 2))


score = 0

score += 1
print("Yor score is " + str(score))



score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height} You are winnis is {is_winning}")

"""

print("Welcome to the tip calculator!")

bill = float(input("Whats was the total bill? "))
tip = int(input("How musch tip would you like to give? 10, 12 or 15%? "))
people = int(input("How many people to split the bill? "))

bill_With_Tip = tip / 100 * bill + bill

total_per_person = bill_With_Tip / people
total = round(total_per_person, 2)
print(f"Each person should pay ${total}")