# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = None ):
        self.name = name
        self.description = description
        self.items = items
    def getRoom(self):
        return f"Name: {self.name}\nDescription: {self.description}\nItems:\n{self.printItems()}"
    def printItems(self):
        if self.items == None: 
            return ""
        else: 
            return "\n".join(map(str, self.items))
    def getItem(self, item):
        for v in self.items:
            if item == v.name:
                return v
        return None
    def removeItem(self, item):
        self.items.pop(self.items.index(item))
    def addItem(self, item):
        self.items.append(item)