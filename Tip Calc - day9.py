#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = 150.00
tip = .12
total_bill = bill * tip
total_bill = total_bill + bill
people = 5
total_bill = total_bill / people
print(f"Each person should pay ${total_bill:.2f}")
