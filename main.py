import db

coffee_types = list(db.MENU)
money = 0


def check_resource(choice):
    required = db.MENU[choice]["ingredients"]
    for r, v in required.items():
        if v > db.resources[r]:
            print(f"“Sorry there is not enough {r}.")
            return False
    # not updating the resource right here as total money is not checked now.
    return True


def update_resource(choice):
    required = db.MENU[choice]["ingredients"]
    for r, v in required.items():
        db.resources[r] -= v


while True:
    print("-------------------------------------------------")
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {db.resources['water']}ml")
        print(f"Milk: {db.resources['milk']}ml")
        print(f"Coffee: {db.resources['coffee']}gm")
        print(f"Money: ${money}")
        print("--------------------------")
    elif choice in coffee_types and check_resource(choice):
        cost = db.MENU[choice]["cost"]
        print("Please insert coins:")
        total = 0
        for i, v in db.COINS.items():
            total += v * float(input(f"How many {i}? "))
        if total < cost:
            print("“Sorry that's not enough money. Money refunded.")
        else:
            money += cost
            print(f"Here is ${round(total - cost, 2)} dollars in change.")
            update_resource(choice)
    print(f"“Here is your {choice}. Enjoy")