# TODO: 2. Check resources sufficient to make drink order

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

money = 0

machine_on = True

technician_called = False


def report():
    """Prints state of machine at the moment."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {round(money, 3)}")


def check_resources(drink_name):
    """Checks that there's enough water, milk and coffee in the machine to complete the order. Returns True or Flase."""
    for ingredient in MENU[drink_name]['ingredients']:
        if resources[ingredient] >= MENU[drink_name]['ingredients'][ingredient]:
            return True
        else:
            return False


def make_drink(drink_name):
    """Calls check_resources() and subtracts the drinks ingredients from the machine's resources if it passes. If it
    fails, sets the call_technician flag to True and returns False."""
    global technician_called
    print(f"Making {drink_name}")
    if check_resources(drink_name):
        for ingredient in MENU[drink_name]['ingredients']:
            resources[ingredient] -= MENU[drink_name]['ingredients'][ingredient]
    else:
        for ingredient in resources:
            if resources[ingredient] < MENU[drink_name]['ingredients'][ingredient]:
                print(f"Sorry, there is not enough {ingredient} to make your {drink_name}.")
        print(f"Machine is out of order. A technician has been called. Please try again later.")
        technician_called = True
        return False


def take_payment(drink_name):
    """Requests payment for the drink selected by the user and calculates change if necessary. Adds payment to machine's
    total money. Refunds money and returns False if not enough money added to pay for drink."""
    global money
    print(f"You have selected {drink_name}.")
    print(f"Please insert ${MENU[drink_name]['cost']}")
    total_in = int(input("How many quarters: ")) * 0.25
    if total_in < MENU[drink_name]['cost']:
        total_in += int(input("How many dimes: ")) * 0.10
        if total_in < MENU[drink_name]['cost']:
            total_in += int(input("How many nickels: ")) * 0.5
            if total_in < MENU[drink_name]['cost']:
                total_in += int(input("How many pennies: ")) * 0.01
    change = total_in - MENU[drink_name]['cost']
    if total_in > MENU[drink_name]['cost']:
        print(f"Please take your change of ${round(change, 2)} and wait for your {drink_name} to be dispensed below.")
        money += round(MENU[drink_name]['cost'], 2)
        return make_drink(drink_name)
    elif total_in == MENU[drink_name]['cost']:
        print(f"Please wait for your {drink_name} to be dispensed below")
        money += round(MENU[drink_name]['cost'], 2)
        return make_drink(drink_name)
    else:
        print(f"Insufficient funds. Please make another selection and try again.")
        print(f"Machine returns your ${total_in} to you.")
        total_in = 0
        return False


while machine_on:
    while not technician_called:
        # TODO: 1. Prompt user by asking "what would you like?" - this should be the default state of the machine
        user_selection = input("What would you like? (espresso/latte/cappuccino)")

        # TODO: 2. Turn off coffee machine by entering "off" to the prompt
        if user_selection == "off":
            machine_on = False
            exit()
        # TODO: 3. Print report on current state of machine when user types "report"
        elif user_selection == "report":
            report()
        # TODO: 4. Allow a technician to reset the machine.
        elif user_selection == "service":
            technician_called = False
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }
            money = 0
        elif user_selection == "cappuccino" or user_selection == "latte" or user_selection == "espresso":
            take_payment(user_selection)
        else:
            print("Invalid selection.\nPlease try again.")
    out_of_order = input("Out of order. Please enter service code.")
    if out_of_order == "service":
        technician_called = False
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        money = 0
    else:
        print("Incorrect service code entered. Please try again.")