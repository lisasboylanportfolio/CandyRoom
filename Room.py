class Room:

    def __init__(self,name,description,inventory=None,archFeatures=None,actions=None, adjacentRooms=None, toAccess=None):
        self.name=name
        self.description=description
        self.inventory=inventory
        self.originalarchFeatures=archFeatures        
        self.archFeatures=archFeatures
        self.actions=actions
        self.adjacentRooms=adjacentRooms
        self.toAccess=toAccess
    
    def addInventory(self, item):
        self.inventory.append(item)
        
    def removeInventory(self, item):
        if self.hasInventoryItem(item):
            self.inventory.remove(item)
        
    def hasInventoryItem(self, item):
        # Check if element exist in List, before removing
        if self.inventory != None:
            if item in self.inventory:
                return True
            else:
                return False
        else:
            return False
        
    def getOriginalArchFeatures():
        return self.originalArchFeatures
    
    def getArchFeatures():
        return self.archFeatures
    
    def removeArchFeatures(self, item):
        if len(self.archFeatures) > 0:
            del self.archFeatures[item]
            
    def resetArchFeatures():
        self.archFeatures = self.originalArchFeatures