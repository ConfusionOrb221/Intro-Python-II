# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, inventory = []):
        self.name = name
        self.room = room
        self.inventory = inventory
    def setRoom(self, room):
        self.room = room
    def addItem(self, item):
        self.inventory.append(item)
    def getItem(self, item):
        for v in self.inventory:
            if item == v.name:
                return v
        return None
    def removeItem(self, item):
        return self.inventory.pop(self.inventory.index(item))
    def getInventory(self):
        return "\n".join(map(str, self.inventory))