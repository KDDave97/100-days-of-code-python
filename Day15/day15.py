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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def handle_inputs():
    action = input("What would you like to do? (espresso/latte/cappuccino): ").lower()
    while action != "espresso" and action != "latte" and action != "cappuccino" and action != "report" and action != "off":
        action = input("What would you like to do? (espresso/latte/cappuccino): ").lower()
    if action == "espresso" or action == "latte" or action == "cappuccino":
        check_availability(action)
    elif action == "report":
        report_print()
    elif action == "off":
        exit()

def report_print():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")
    handle_inputs()

def check_availability(order):
    for ingredient in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, missing {ingredient}")
            handle_inputs()
    handle_orders(order)

def handle_orders(order):
    quarter = float(input("How many quarters? ($0.25): ")) * 0.25
    dimes = float(input("How many dimes? ($0.10): ")) * 0.10
    nickles = float(input("How many nickles? ($0.05): ")) * 0.05
    pennies = float(input("How many pennies? ($0.01): ")) * 0.01
    total = quarter + dimes + nickles + pennies
    if total < MENU[order]["cost"]:
        print(f"Sorry, thats not enough money! {order} costs ${MENU[order]["cost"]}. Your ${total} has been refunded.")
    else:
        change = total - MENU[order]["cost"]
        print(f"Here is ${round(change, 2)} in change!")
        print(f"Here is your {order}. Enjoy!")
        refresh_stock(order)

def refresh_stock(order):
    global profit
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    profit += MENU[order]["cost"]
    handle_inputs()

handle_inputs()
