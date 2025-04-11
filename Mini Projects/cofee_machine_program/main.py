MENU = {
    "espresso": {
        "ingredients": {
            "water": 500,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
profit = 0


def is_order_ingredient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is no enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    "Return True when payment is accepted , or False if money is insufficient."
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    "Deduct the required ingredients from the resources."
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your  {drink_name}☕")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("machine is turning off")
        is_on = False
    elif choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney : {profit}")

    else:
        if choice in MENU:
            drink = MENU[choice]
            
            if not is_order_ingredient(drink['ingredients']):
                print("Beep! Beep! Insufficient resources. Turning off the machine ")
                is_on = False
                break

            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid selection. Please choose a valid option.")

