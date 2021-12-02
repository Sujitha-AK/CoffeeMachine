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


def using_resource(getting_coffee):
    if getting_coffee == "latte" or getting_coffee == "cappuccino":
        if resources['water'] >= MENU[getting_coffee]['ingredients']['water'] and resources['milk'] >= MENU[getting_coffee]['ingredients']['milk'] and resources['coffee'] >= MENU[getting_coffee]['ingredients']['coffee']:
            resources_water = resources['water'] - MENU[getting_coffee]['ingredients']['water']
            resources['water'] = resources_water
            resources_milk = resources['milk'] - MENU[getting_coffee]['ingredients']['milk']
            resources['milk'] = resources_milk
            resources_coffee = resources['coffee'] - MENU[getting_coffee]['ingredients']['coffee']
            resources['coffee'] = resources_coffee
            process_coins(getting_coffee)
        elif resources['water'] < MENU[getting_coffee]['ingredients']['water']:
            print("Sorry there is no enough water.")
        elif resources['milk'] < MENU[getting_coffee]['ingredients']['milk']:
            print("Sorry there is no enough milk.")
        elif resources['coffee'] < MENU[getting_coffee]['ingredients']['coffee']:
            print("Sorry there is no enough coffee powder.")
    else:
        if resources['water'] >= MENU[getting_coffee]['ingredients']['water'] and resources['coffee'] >= MENU[getting_coffee]['ingredients']['coffee']:
            resources_water = resources['water'] - MENU[getting_coffee]['ingredients']['water']
            resources['water'] = resources_water
            resources_coffee = resources['coffee'] - MENU[getting_coffee]['ingredients']['coffee']
            resources['coffee'] = resources_coffee
            process_coins(getting_coffee)
        elif resources['water'] < MENU[getting_coffee]['ingredients']['water']:
            print("Sorry there is no enough water.")
        elif resources['coffee'] < MENU[getting_coffee]['ingredients']['coffee']:
            print("Sorry there is no enough coffee powder.")


def process_coins(getting_coffee):
    print("Please insert the coins.")
    quarters_coins = int(input("how many quarters? "))
    dimes_coins = int(input("how many dimes? "))
    nickles_coins = int(input("how many nickles? "))
    penny_coins = int(input("how many pennies? "))
    total_amount = (0.25 * quarters_coins) + (0.10 * dimes_coins) + (0.05 * nickles_coins) + (0.01 * penny_coins)
    actual_amount = float(MENU[getting_coffee]["cost"])
    remaining_amount = round(total_amount - actual_amount,2)
    if total_amount < actual_amount :
        print("sorry that's not enough money. Money refunded.")
    else :
        print(f"Here is ${remaining_amount} in change.")
        print(f"Here is your {getting_coffee}. ☕ Enjoy!")


sufficient_amount = True
while sufficient_amount :
    getting_coffee = input("what would you like? (espresso/latte/cappuccino): ")
    if getting_coffee == "off":
        sufficient_amount = False

    elif getting_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif getting_coffee == "espresso":
        using_resource("espresso")
        profit = profit+1.5

    elif getting_coffee == "latte":
        using_resource("latte")
        profit = profit + 2.5

    elif getting_coffee == "cappuccino":
        using_resource("cappuccino")
        profit = profit + 3.0


