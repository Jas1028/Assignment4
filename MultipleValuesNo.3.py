# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

print("Good day Ma'am and Sir,")
print("Enjoy Buying! Have a nice day :) ")


def AmountOfMoneyYouHaveAndPriceOfAnApple():
    Money = int(input("How much money do you have? "))
    Price = int(input("What is the price of an apple? "))
    return Money, Price


def MaximumNumberOfApplesAndTheRemainingMoney(AmountOfMoney_,PriceOfAnApple_):
    MaximumNumber = int(AmountOfMoney_) // (PriceOfAnApple_)
    RemainingMoney = int(AmountOfMoney_) % (PriceOfAnApple_)
    return MaximumNumber, RemainingMoney
   
def DisplayOutput(MaximumNUmberOfAnApple_, RemainingMoneyYouWillHave_):
    print(f"You can buy {MaximumNUmberOfAnApple_ } apples and your change is {RemainingMoneyYouWillHave_} pesos. ")

    
#Steps
#1. Enter the amount of money you have and ask for the price of an apple.
AmountOfMoney, PriceOfAnApple = AmountOfMoneyYouHaveAndPriceOfAnApple()
#2. Display the maximum number of apples that you can buy and the remaining money that you will have.
MaximumNUmberOfAnApple, RemainingMoneyYouWillHave = MaximumNumberOfApplesAndTheRemainingMoney(AmountOfMoney,PriceOfAnApple)
#3. Display the output.
DisplayOutput(MaximumNUmberOfAnApple, RemainingMoneyYouWillHave)