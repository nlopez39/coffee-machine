from coffee import MENU
from coffee import resources

money = 0

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        #if water,milk, or coffee from lets say latte is greater than the report resources then ...
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}. Choose another drink")
            return False
    return True

def process_coins():
    """Returns the total of the payment"""
    print("Please insert coins.")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.10
    total += int(input("how many nickels?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total
def transaction_successful(payment, drink_price):
    """Return true when payment is sufficient/as well as change if too much money and false if payment is insufficcient"""
    #if payment is enough or greater than the price of drink than
    if payment >= drink_price:
        change = payment - drink_price
        #change = round(payment-drink_price,2)2 places
        print(f"You gave me {payment}. Your change is {change}")
        global money
        money += payment

    else:
        #that is not enough money for the drink
        print("Sorry not enough. Money refunded")
def make_coffee(order_ingredients, drink_name):
    """DEduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        return resources[item]
    print(f"Here is your {drink_name}. Enjoy!")



#driver code
done = False
while not done:
    choice = input("What would you like? (espresso $1.50/latte $2.50 /cappuccino $3.00):")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}mg")
        print(f"Money: ${money}")
    elif choice =="off":
        done = True
    else:
         #it is a drink
        drink = MENU[choice]#this looks for the type of drink in the MENU
        #check if resources are sufficient/ which will allow us to make the coffee
        if check_resources(drink['ingredients']) == True:
            payment = process_coins()
            transaction_successful(payment, drink['cost'])
            make_coffee(drink['ingredients'], choice)









