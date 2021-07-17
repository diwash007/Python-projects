MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

not_off = True


def view_report():
    print(f"water : {resource['water']}ml")
    print(f"milk : {resource['milk']}ml")
    print(f"coffee : {resource['coffee']}gm")
    print(f"money : ${resource['money']}")


def ask_coins(coin):
    return int(input(f"How many {coin}? "))


def calculate_money():
    print("\nPlease insert coins.")
    return ask_coins("quarters") * 0.25 + ask_coins("dimes") * 0.1 + ask_coins("nickels") * 0.05 + ask_coins("pennies") * 0.01


def manage_resource(coffee):
    if resource["milk"] > coffee["ingredients"]["milk"] and resource["water"] > coffee["ingredients"]["water"] and resource["coffee"] > coffee["ingredients"]["coffee"]:
        resource["milk"] -= coffee["ingredients"]["milk"]
        resource["water"] -= coffee["ingredients"]["water"]
        resource["coffee"] -= coffee["ingredients"]["coffee"]
        return False
    else:
        print("Sorry, there is not enough resources!")
        return True


def check_money(money, coffee):
    if money >= coffee["cost"]:
        resource["money"] += coffee["cost"]
        change = money - coffee["cost"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}, enjoy!!")
    else:
        print("Sorry that's not enough money!!")
        return 0


def make_coffee(coffee):
    no_resource = manage_resource(coffee)
    if not no_resource:
        money = calculate_money()
        check_money(money, coffee)
    

def input_processor(choice):
    if choice == "report":
        view_report()
    elif choice == "off":
        return False
    elif choice == "latte":
        make_coffee(MENU["latte"])
    elif choice == "espresso":
        make_coffee(MENU["espresso"])
    elif choice == "cappuccino":
        make_coffee(MENU["cappuccino"])
    else:
        print("Invalid Input!!")
    return True

    
while not_off:

    choice = input("\nWhat would you like? (espresso/latte/cappuccino)").lower()

    not_off = input_processor(choice)

