from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Nathan", room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def goDirection(player):
    while True:
        direction = input('Enter a cardinal direction: ')
        direction = direction.lower()
        try:
            if direction == 'n':
                return player.setRoom(player.room.n_to)
            elif direction == 'e':
                return player.setRoom(player.room.e_to)
            elif direction == 's':
                return player.setRoom(player.room.s_to)
            elif direction == 'w':
                return player.setRoom(player.room.w_to)
            else:
                raise Exception('Not a valid cardinal direction')
        except:
            print("Cant go there")


def parseInput():
    while True:
        print(player.room.getRoom())

        goDirection(player)

parseInput()

"""
'n': player.setRoom(player.room.n_to),
'e': player.setRoom(player.room.e_to),
's': player.setRoom(player.room.s_to),
'w': player.setRoom(player.room.w_to)
"""

