from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: Print report
folger = CoffeeMaker()
atm = MoneyMachine()
folger.report()
atm.report()
# TODO: Check resources sufficiency
menu = Menu()
is_on = True
while is_on:
    order = input("Please select a drink: " + menu.get_items())
    if order == 'off':
        is_on = False
    elif order == 'report':
        atm.report()
        folger.report()
    else:
        drink = menu.find_drink(order)
        if folger.is_resource_sufficient(drink):
            # TODO: Process coins
            # input_coins = atm.process_coins()
            # TODO: Check transaction
            if atm.make_payment(drink.cost):
                # TODO: Make coffee
                folger.make_coffee(drink)