#Curtis Felsher

# Displays instructions for players to input
def show_instructions():
    # Print how to play
    print("Welcome to Alien Infestation!")
    print("An alien infestation has taken hold in a derelict spaceship!")
    print("Collect all 6 items and reach the Medical Bay to win the game or be killed by the alien infestation!")
    print("Movement commands: South, North, East, West")
    print("Add to Inventory: Enter Y or N\n")


# Main function
def main():
    # Calling function to display gameplay instructions
    show_instructions()
    # A dictionary linking a room to other rooms
    # and displaying one item for each room
    rooms = {'Mess Hall': {'South': 'Decontamination Chamber', 'North': 'Navigation Room', 'East': 'Power Station', 'West': 'Kitchen', 'item': 'Flashlight'},
             'Decontamination Chamber': {'North': 'Mess Hall', 'East': 'Docking Station', 'item': 'Oxygen Tank'},
             'Docking Station': {'West': 'Decontamination Chamber', 'item': None},
             'Medical Bay': {'South': 'Power Station', 'item': 'Alien'},
             'Navigation Room': {'East': 'Command Deck', 'South': 'Mess Hall', 'item': 'Ammo Crate'},
             'Kitchen': {'East': 'Mess Hall', 'item': 'Crowbar'},
             'Command Deck': {'West': 'Navigation Room', 'item': 'Electrical Fuse'},
             'Power Station': {'West': 'Mess Hall', 'North': 'Medical Bay', 'item': 'Ray Gun'}
             }

    # Starting room
    current_room = 'Docking Station'
    # List to hold collected items
    inventory = []

    # Loop to show movement between rooms
    while True:
        # If current_room is Medical Bay, this breaks the loop
        if current_room == 'Medical Bay':
            print("\nYou are in the", current_room)
            print("\nAn alien infestation has taken hold!", )
            if len(inventory) == 6:
                print("\nYou have destroyed the alien infestation! Congratulations!")
            else:
                print("\nThe alien infestation has killed you! Game Over!")
            break

        # Displays current_room
        print("\nYou are in the", current_room)

        # Asks player if they would like to pick up the current rooms item
        if rooms[current_room]['item'] != None:
            print("You see a", rooms[current_room]['item'], 'on the floor.')
            opinion = input("Pick up " + rooms[current_room]['item'] + "?(Y/N): ").upper()
            # Validating user input
            while opinion not in ['Y', 'N']:
                print("Invalid selection. Try again")
                opinion = input("Pick up " + rooms[current_room]['item'] + "?(Y/N): ").upper()
            if opinion == 'Y':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        else:
            print("Item already collected or nothing in this room.")

        # Displays current inventory
        print("Inventory:", inventory)

        # Asks player which direction they would like to move
        direction = input("Which direction would you like to go?(East,West,North,South): ").title()
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        # Validating direction
        while direction not in directions:
            print("There is a wall in that direction. Try again")
            direction = input("Which direction would you like to go?(East,West,North,South): ").title()

        # Setting next_room
        next_room = rooms[current_room][direction]
        print("Moving to the", next_room)
        print("-----------------------------------------------------------------------------------")

        # Updating current_room
        current_room = next_room

    # Printing end message
    print("\nThank you for playing Alien Infestation. I hope you have a wonderful week! :)")


# Calling main function
main()