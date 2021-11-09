# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

print("Good day! Ma'am and Sir,")
print("We are offering you an affordable and fresh apples and juicy oranges. Enjoy buying! ")
ApplePrice = 20
OrangePrice = 25

def AskHowManyApplesOrangesYouWantToBuy():
    PreferredApple = int(input("An apple cost 20 pesos each. How many apple/s do you prefer to buy? "))
    PreferredOrange = int(input("An orange cost 25 pesos. How many orange/s do you prefer to buy? "))
    return PreferredApple, PreferredOrange
# Steps
# 1. Ask how many apples and oranges you want to buy
NumberOfAppleAndOrange = AskHowManyApplesOrangesYouWantToBuy()
