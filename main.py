from src.menu import Menu, MenuItem
from src.coffee_maker import CoffeeMaker
from src.money_machine import MoneyMachine

""""
requirement for program
1. print report
2. check resources sufficient?
3. process coins
4. check transaction successful
5. make cofeee
"""
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_shop_on = True
#coffee_maker.report()
while coffee_shop_on:
    report = menu.get_items()
    order_item = menu.find_drink(input(f"Order Please menu are {report}: "))
    print(order_item)
    if order_item and coffee_maker.is_resource_sufficient(order_item):
        money_machine.make_payment(order_item.cost) 
    on = input("you wannna have something more. type y for yes, anything else for no: ").lower
    if on != 'y':
        coffee_shop_on= False


