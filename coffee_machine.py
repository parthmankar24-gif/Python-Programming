MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
            "water": 250,
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


def is_sufficient(order):
    for item in order:
        if order[item] >= resources[item]:
            return False
    return True

def coins():
    print("Please Enter Coins: ")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def sufficient_coins(entered_cost, drink_cost):
    if entered_cost >= drink_cost:
        change = entered_cost - drink_cost
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(drink_item, ordered_item):
    for item in ordered_item:
        resources[item] -= ordered_item[item]
    print(f"Here is your {drink_item}.....")


profit = 0
is_true = True
while is_true:
    choice = input("What would you like? (expresso / latte / cappuccino): ").lower()
    if choice == "off":
        is_true = False
    elif choice == "report":
        print(f"Water:-{resources['water']} ml")
        print(f"Milk:- {resources['milk']}ml")
        print(f"Coffee:- {resources['coffee']}g")
        print(f"Money:- {profit}")

    else:
        desc = MENU[choice]
        if is_sufficient(desc["ingredients"]):
            payment = coins()
            if sufficient_coins(payment, desc["cost"]):
                make_coffee(choice, desc["ingredients"])
