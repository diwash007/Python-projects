from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


c_menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
not_off = True

while not_off:
    choice = input(f"\nWhat do you like? {c_menu.get_items()[:-4]}?")

    item = c_menu.find_drink(choice)

    if choice == "report":
        cm.report()
        mm.report()
    elif choice == "off":
        not_off = False
    elif item == None:
        print("Sorry that item is not available.")
    else:
        if cm.is_resource_sufficient(item):
            is_enough = mm.make_payment(item.cost)
            if is_enough:
                cm.make_coffee(item)
