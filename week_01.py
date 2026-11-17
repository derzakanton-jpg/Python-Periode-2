
player_name = input("What is your name?")
player_gold = 100
inventory = []

print("Welcome to the Fantasy Item Shop!")
print("Hallo", player_name, "! You have", player_gold, "gold.")

items = [
    ["Sword", 50],
    ["Shield", 40],
    ["Potion", 20],
    ["Bow", 60],
    ["AK-47", 55],
    ["Knife", 45]
]

shop_open = True

while shop_open:
    print("\n========== FANTASY ITEM SHOP ==========")

    number = 1
    for item in items:
        print(f"{number}. Buy {item[0]} ({item[1]} gold)")
        number = number + 1

    print("---------------------------------------")
    print("7. View inventory")
    print("8. Exit shop")
    print("---------------------------------------")

    choice = input("What would you like to do? ")

    # stupid Inventory
    if choice == "7":
        print("\n========== YOUR INVENTORY ==========")

        if len(inventory) == 0:
            print("Your inventory is empty!")
        else:
            for item in items:
                count = inventory.count(item[0])
                if count > 0:
                    print(item[0], "x", count)

        print("Gold:", player_gold)
        input("Press Enter to return to the shop...")
        continue

  #shop
    match choice:
        case "1":
            amount = int(input("How many Swords? "))
            total_price = 50 * amount

            if amount > 0 and player_gold >= total_price:
                player_gold = player_gold - total_price
                for i in range(amount):
                    inventory.append("Sword")
                print("You bought", amount, "Sword(s)!")
                print("You have", player_gold, "gold left.")
            else:
                print("You don't have enough gold or invalid amount!")

        case "2":
            amount = int(input("How many Shields? "))
            total_price = 40 * amount

            if amount > 0 and player_gold >= total_price:
                player_gold = player_gold - total_price
                for i in range(amount):
                    inventory.append("Shield")
                print("You bought", amount, "Shield(s)!")
                print("You have", player_gold, "gold left.")
            else:
                print("You don't have enough gold or invalid amount!")

        case "3":
            amount = int(input("How many Potions? "))
            total_price = 20 * amount

            if amount > 0 and player_gold >= total_price:
                player_gold = player_gold - total_price
                for i in range(amount):
                    inventory.append("Potion")
                print("You bought", amount, "Potion(s)!")
                print("You have", player_gold, "gold left.")
            else:
                print("You don't have enough gold or invalid amount!")

        case "4":
            amount = int(input("How many Bows? "))
            total_price = 60 * amount

            if amount > 0 and player_gold >= total_price:
                player_gold = player_gold - total_price
                for i in range(amount):
                    inventory.append("Bow")
                print("You bought", amount, "Bow(s)!")
                print("You have", player_gold, "gold left.")
            else:
                print("You don't have enough gold or invalid amount!")

        case "5":
            amount = int(input("How many AK-47s? "))
            total_price = 55 * amount

            if amount > 0 and player_gold >= total_price:
                player_gold = player_gold - total_price
                for i in range(amount):
                    inventory.append("AK-47")
                print("You bought", amount, "AK-47(s)!")
                print("You have", player_gold, "gold left.")
            else:
                print("You don't have enough gold or invalid amount!")

        case "6":
            amount = int(input("How many Knives? "))
            total_price = 45 * amount

            if amount > 0 and player_gold >= total_price:
                player_gold = player_gold - total_price
                for i in range(amount):
                    inventory.append("Knife")
                print("You bought", amount, "Knife(s)!")
                print("You have", player_gold, "gold left.")
            else:
                print("You don't have enough gold or invalid amount!")

        case "8":
            shop_open = False
            print("\nThanks for visiting,", player_name, "!")
            print("You have", player_gold, "gold left.")
            print("See you next time!")

        case _:
            print("Invalid choice! Please choose 1-8.")


