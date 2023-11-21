from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

fast_coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
coffee_menu = Menu()

choice1 = "on"


while choice1 != "off":
    choice1 = input(f"What would you like? {coffee_menu.get_items()}: ").lower()

    if choice1 == "report":
        fast_coffee_machine.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice1)      
        if fast_coffee_machine.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost) == True:
                fast_coffee_machine.make_coffee(drink)
        

