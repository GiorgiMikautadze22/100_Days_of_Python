from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = input(f'Which type of coffee do you want {menu.get_items()}?: ')

    if user_choice == "off":
        print('Good By')
        break
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice) is None:
        print(f'Please choose between {menu.get_items()}')
    else:
        coffe_type = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(coffe_type) and money_machine.make_payment(coffe_type.cost):
                coffee_maker.make_coffee(coffe_type)
        



