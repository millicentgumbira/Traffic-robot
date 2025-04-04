import random

name = input("Welcome to treasure hunt 1")
print(name)

locations = {
    "beach": {"description": "You are on a beautiful beach.", "items": ["shell"], "exits": ["jungle"]},
    "jungle": {"description": "You are in a dense jungle.", "items": ["map"], "exits": ["beach", "cave"]},
    "cave": {"description": "You are in a dark cave.", "items": ["treasure"], "exits": ["jungle"]}
}


current_location = "beach"
inventory = []

while True:
    print(locations[current_location]["description"])

    if locations[current_location]["items"]:
        print("You see the following items:")
        for item in locations[current_location]["items"]:
            print(item)

    print("You can go to the following locations:")
    for exit in locations[current_location]["exits"]:
        print(exit)

    action = input("What do you want to do? ").lower()

    if action in locations[current_location]["items"]:
        inventory.append(action)
        locations[current_location]["items"].remove(action)
        print("You picked up the", action)
    elif action in locations[current_location]["exits"]:
        current_location = action
    elif action == "inventory":
        print("You are carrying:")
        for item in inventory:
            print(item)
    elif action == "quit":
        break
    else:
        print("Invalid action. Try again.")

    if "treasure" in inventory:
        print("Congratulations! You found the treasure!")
        break
