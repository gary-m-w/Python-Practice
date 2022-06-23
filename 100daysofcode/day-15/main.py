MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}

on = True


# TODO: 1. print a report
def get_report():
    print(f"Water: {resources['water']}mL\n"
          f"Milk: {resources['milk']}mL\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")


def get_input():
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'report':
        get_report()
        run_coffee()
    if user_input == 'off':
        print("Shutting down...")
        exit()
    else:
        return user_input


# TODO 2. check resources for sufficiency
def check_resources(coffee_type):
    if MENU[coffee_type]['ingredients']['water'] <= resources['water']:
        if MENU[coffee_type]['ingredients']['milk'] <= resources['milk']:
            if MENU[coffee_type]['ingredients']['coffee'] <= resources['coffee']:
                coin_process(coffee_type)
            else:
                print('Sorry, there is not enough coffee.')
                run_coffee()
        else:
            print("Sorry, there is not enough milk.")
            run_coffee()
    else:
        print("Sorry, there is not enough water")
        run_coffee()


# TODO 3. process coins
def coin_process(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    # TODO 4. check transaction successful
    if total >= MENU[coffee_type]['cost']:
        change = round((total - MENU[coffee_type]['cost']), 2)
        global resources
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        resources['money'] += MENU[coffee_type]['cost']
        # TODO 5. make coffee
        print(f"Here is ${change} in change.\nHere is your {coffee_type}. Enjoy!")
        run_coffee()
    else:
        print("Sorry, that's not enough money. Money refunded.")
        run_coffee()


def run_coffee():
    coffee = get_input()
    check_resources(coffee)


run_coffee()