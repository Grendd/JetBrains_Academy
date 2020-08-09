water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def buying():
    global water
    global coffee
    global cups
    global milk
    global money
    choice_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if choice_coffee == "1":
        if water > 250 and coffee > 16 and cups > 1:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee -= 16
            cups -= 1
            money += 4
        coffee_machine()
    elif choice_coffee == "2":
        if water > 350 and coffee > 16 and cups > 1 and milk > 75:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
            money += 7
        elif water < 350:
            print("Sorry, not enough water!")
        coffee_machine()
    elif choice_coffee == "3":
        if water > 200 and coffee > 12 and cups > 1 and milk > 100:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee -= 12
            cups -= 1
            money += 6
        coffee_machine()
    elif choice_coffee == "back":
        coffee_machine()


def filling():
    global water
    global coffee
    global cups
    global milk
    water_fill = int(input("Write how many ml of water do you want to add:"))
    milk_fill = int(input("Write how many ml of milk do you want to add:"))
    coffee_fill = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_fill = int(input("Write how many disposable cups of coffee do you want to add:"))
    water += water_fill
    milk += milk_fill
    coffee += coffee_fill
    cups += cups_fill
    coffee_machine()


def taking():
    global money
    print("I gave you $" + str(money))
    money = 0
    coffee_machine()


def stats_print():
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")


def coffee_machine():
    user_action = input("Write action (buy, fill, take, remaining, exit):")
    if user_action == "buy":
        buying()
    elif user_action == "fill":
        filling()
    elif user_action == "take":
        taking()
    elif user_action == "remaining":
        stats_print()
        coffee_machine()
    elif user_action == "exit":
        return


coffee_machine()