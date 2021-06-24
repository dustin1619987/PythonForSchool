#Dustin William Price
#Start of Code
# Defining the game instructions
def game_instructions():
    print('Haunted House Text Adventure Game')
    print('Collect 6 items to win the game, or be eaten by the Ghostly Villain.')
    print('Move Commands: North, East, South, West, exit')
    print('Add to Inventory: get "item" ')
    print('--------------------------------------')

# Dictionary for Rooms & Items
rooms = {
    'Front Room': {'East': 'Dining Room'},
    'Dining Room': {'North': 'Bedroom', 'East': 'Living Room', 'South': 'Kitchen', 'West': 'Front Room',
                    'item': 'Flashlight'},
    'Bedroom': {'East': 'Kids Playroom', 'South': 'Dining Room', 'item': 'Container'},
    'Kids Playroom': {'West': 'Bedroom', 'item': 'Disposable Camera'},
    'Kitchen': {'North': 'Dining Room', 'East': 'Basement', 'item': 'Protein Bar'},
    'Basement': {'West': 'Kitchen', 'item': 'Matches'},
    'Living Room': {'North': 'Master Bedroom', 'West': 'Dining Room', 'item': 'Amulet'},
    'Master Bedroom': {'South': 'Living Room', 'item': 'Ghostly Villain'},
    'Exit': {'exit': 'exit'}
}


# Def for add_to_inventory
def add_to_inventory(item, inventory, currentRoom):
    if item == rooms[currentRoom]['item']:
        inventory.append(item)
        del rooms[currentRoom]['item']
    else:
        print(item, 'not in the', currentRoom)

    return inventory

# Def for move_between_rooms
def move_between_rooms(currentRoom, move, rooms):
    currentRoom = rooms[currentRoom][move]
    return currentRoom

# Current room Starts at Front Room
currentRoom = 'Front Room'
# Inventory variable holder
inventory = []
# Calling  Game Insructions
game_instructions()

# While Loop for being True
item_you_see = ""
while True:

    print('You are in the', currentRoom)
    print('Inventory', inventory)
    print('--------------------------------------')

    # When the player finds a item in the room that is not the ghost.
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] != 'Ghostly Villain':
        item_you_see = rooms[currentRoom]['item']
        print('You see a', item_you_see)
        print('--------------------------------------')

    # input move(either direction, get item or exit)
    move = input("Enter your move: ").lower()
    if 'get' in move and item_you_see != "":
        item = (' ').join(move.split()[1:])
        item = item.title()
        inventory = add_to_inventory(item, inventory, currentRoom)
        if item in inventory:
            item_you_see = ""
    # if not then move directions then else wrong
    elif move in ('north', 'east', 'south', 'west'):
        direction = move.title()
        if direction in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][direction]
        else:
            print('Wrong direction...Try again!')
            continue
    # if player inputs exit - To exit the game
    elif move == 'exit':
        break
    else:
        print('Wrong move...Try again!')
        continue

    # If in MasterBedroom
    if currentRoom == 'Master Bedroom':
        # Could Comment these two lines out but keeping it to have like a ending Stat thing
        print('You are currently in the', currentRoom)
        print('Inventory:', inventory)

        # If the inventory had less then 6 then you loose the game Prints game lose logs
        if len(inventory) != 6:
            print('Ahhhh Nooo... You have enter into the Ghostly Villain hiding spot!')
            print('Ghostly Villain Speaks.... You have entered my house without PERMISSION. You shall perish for '
                  'trespassing! *SLASHhhh - Shalshh* WUAHAHAHAHAHAH')
            print('GAME OVER! Better luck next time.')
            break

        # If you have all 6 and in the Master Bedroom Prints winning game log
        else:
            print('You have collected all the items! The Ghostly Villain has shown its self!... So you think you can '
                  'enter my House without PERMISSION!?')
            print('As the Ghost Villain talks... You open your bag and with all the items - crafted machine that can '
                  'knock the ghost out for a period of time! You used the machine to knock the ghostly Villain out!')
            print('Ooo noo.. wait whats that.... WACK!')
            print('You hurry and get out before the Ghostly Villain wakes back up!')
            print('You won! and escaped with the priceless Amulet!')
            break

# End of Code
