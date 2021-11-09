# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

print("Good day! Ma'am and Sir,")
print("We are offering you an affordable fresh apples and juicy oranges. Enjoy buying! Thank you! ")
ApplePrice = 20
OrangePrice = 25 

def AskHowManyApplesOrangesYouWantToBuy():
    PreferredApple = int(input("An apple cost 20 pesos each. How many apple/s do you prefer to buy? "))
    PreferredOrange = int(input("An orange cost 25 pesos. How many orange/s do you prefer to buy? "))
    return PreferredApple, PreferredOrange

def AmountOfFruits(NumberOfApple_, NumberOfOrange_, ApplePrice_, OrangePrice_):
    AmountOfApple = int(NumberOfApple_ * ApplePrice_)
    AmountOfOrange = int(NumberOfOrange_ * OrangePrice_)
    GeneralAmount = int(AmountOfApple + AmountOfOrange)
    return GeneralAmount

def DisplayOutput(TotalAmount_):
     print(f"The total amount is {TotalAmount_}. ")



# Steps
# 1. Ask how many apples and oranges you want to buy
NumberOfApple, NumberOfOrange = AskHowManyApplesOrangesYouWantToBuy()

# 2. Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
TotalAmount = AmountOfFruits(NumberOfApple, NumberOfOrange, ApplePrice, OrangePrice)

# 3. Display the output in the following format.
DisplayOutput(TotalAmount)
