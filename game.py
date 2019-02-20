from Room import *

def move(room):
    if len(room.adjacentRooms) == 1:
        new_room=room.adjacentRooms[0]
    elif len(room.adjacentRooms) > 1:
        print("Where would like to go?")
        new_room=asker(list(room.adjacentRooms))

    if new_room != "stop":
        # Determine if player has access to room, and switch
        room=switchRooms(room,new_room)
    return room
    
def search(room):
    print("\n What would you like to search?")
    not_searched = list(room.archFeatures.keys())
    answer = asker(not_searched)
    
    while answer != "stop" and room.archFeatures[answer] == None and len(not_searched) > 1:
        print("\n Sorry, nothing there. What else would you like to search?")
        not_searched.remove(answer)        
        answer = asker(not_searched)
        
    if (len(not_searched) == 1 and room.archFeatures[answer] == None) or (len(not_searched) == 0) and answer != "stop" :
        print("The", room.name, " has nothing to offer\n")
        print("You should move and search somewhere else")
    elif answer == "stop":
        pass
    else:
        # Add item to inventory and see if access granted to adjacent rooms
        addInventory(room, answer)
        # loop through adjacent rooms to determine if item grants access
        for aRoom in room.adjacentRooms:
            if rooms[aRoom].toAccess != None:
                token = rooms[aRoom].toAccess
                if token in inventory.values():
                    print("You now have access to", aRoom)
                    print("What will you do next?")
                else:
                    print("You can not enter", aRoom, "whithout first finding", token)
                    
def stop(x=None):
    print("Game Over")
    exit()

def addInventory(room, key):
    item = room.archFeatures[key]
    print("\nCongratulations, you found the '",item,"'","\n" )
    if room.inventory != None:
        if item in room.inventory:
            room.archFeatures[key]=None
            room.removeInventory(item)
            inventory[room.name]=item

def hasAccess(to):
    access=False
    to_access=rooms[to].toAccess
    if  to_access == None or to_access in inventory.values(): 
        access=True
    return access

def switchRooms(old,new):
    if hasAccess(new):
        print("\n You have moved to the", new, "\n\n")
        return rooms[new]
    else:
        print("\n You can not move to", new, "until you obtain the", rooms[new].toAccess, "\n\n")        
        return old

inventory={}  # Players inventory, items remove from rooms

rooms = {
    'porch': Room(
        'porch',
'You are standing on the front porch.\n\
You notice it is an ordinary porch, with its insistant "Welcome" front door mat.\n\
To the left of the mat sits a planter containing a, not to health looking, plant and a large rock. \
There is a pleasantly inviting porch swing with fluffy over stuffed pillows. \
Next to the swing, an empty plate sits on a side table\n\
What would you like to do next?: \n',
        inventory=[
            'house key',
        ],
        archFeatures={
            'mat':None,
            'planter':None,
            'rock':None,
            'swing':None,
            'table':'house key',
            'plate':None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=['foyer'],
    ),
    'foyer': Room(
        'foyer',
"Now you are in the Foyer, you have access the Library and Dining Room. You see a closet and \
stairs to the top floor",
        archFeatures={
            'closet':None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },        
        adjacentRooms=['library','dining room', 'stairs up'],
        toAccess='house key',
    ),
    'dining room':Room(
        'dining room',
"Hungry?, Make your self comfortable at the Dining table.\n\
Just dont't expect great service. There is no food laid out on the buffet\n\
and the cook has the day off.\nAnd be careful, the china cabinet is a little rocky",
        archFeatures={
            "dining table": None,
            "buffet table": None,
            "china cabinet": None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop": stop,
},        
        adjacentRooms=['foyer','kichen'],                
    ),
    'kitchen': Room(
        'kitchen',
"Well, since the cook has the day off, perhaps you would like to help out.\n\
All the amenities are here, refrigerator, stove, dishwasher.\n\
You can find dishes and pots and pans in the cabinets.\n\
Aso, if you wouldn't mind, answering the phone if it rings....Thanks\n",
        archFeatures={
            "cabinets": None,
            "refridgerator": None,
            "stove": None,
            "dishwasher":None,
            "phone": None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=['dining room','stairs up'],                
    ),
    'stairs up':  Room(
        'stairs up',
"Wow, you really get around. Now that you have reached the second floor hallway,\n\
you might as well checkout the two bedrooms with an adjoining bath and\n\
the master bedroom. If you want to go back down stairs, you can either take the\n\
foyer or kitchen stairs\n",
        archFeatures=None,
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["bunk room","bathroom", "queen room", "master room", "kitchen", "foyer"], 
    ),
    'hallway':  Room(
        'hallway',
"Back to the second story hallway. \n\
Again, you can checkout the two bedrooms with an adjoining bath and the master bedroom. \
If you want to go back down stairs, you can either take the foyer or kitchen stairs\n",
        archFeatures=None,
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["bunk room","bathroom", "queen room", "master room", "kitchen", "foyer"],
    ),    
    'library':  Room(
        'library',
"Ahhh, a chance to grab a book from the bookcase and sit back and relax in front of a fire. \
Although, that portrait over the mantel may give you shivers, is it watching you? \
Maybe, it would be better to sit at the desk facing out the window and reflect on your search so far. \
But after that freaky portrait, you may not want to sit with your back to a closet\n",
        archFeatures={
            "fire place": None,
            "bookcase":None,
            "desk":None,
            "portrait":None,
            "closet": "secret stairs",
            "mantel":None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["foyer", "closet"], 
    ),
    'closet':  Room(
        'closet',
"Hmmm, this is interesting. Not a closet at all, but another staircase",
        archFeatures=None,
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["library","secret stairs"],
    ),
    'secret stairs':  Room(
        'secret stairs',
"Congratulations. Feast upon the fruits of your labor.  Before you are bins and jars full of:\n\
        'Malt Balls',\n\
        'Lemon Drops',\n\
        'Blackberry Cream filled Chocolate',\n\
        'Strawberry Cream filled Chocolate',\n\
        'Toblerone',\n\
        'Pop Rocks'\n\
        'Violet Purple',\n\
        'Taffy',\n\
        'Fudge',\n\
        'Caramel Apples',\n\
        'Chocolate Mints'\n",
        archFeatures=None,
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["library"],
        toAccess="secret key",
    ),    
    'bunk room':  Room(
        'bunk room',
"Now in the Bunk Room, one can't help wonder, how many people live here?.\n\
There are three sets of bunk beds, each with a mantching nightstand next to the bed. \
Each night stand has a matching lamp perched on top. Two dressers flanked by a closet.\n",
        archFeatures={
            "beds":None,
            "nightstands":None,
            "dressers":None,
            "closet":None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["bathroom", "hallway"],
    ),
    'bathroom': Room(
        'bathroom',
"Dispite its size, it is hard to believe this single bathroom with its two sinks, wall length mirror, single toilet and shower, \
could possible function for the number of people each adjoining bedroom could potentially sleep\n",
        archFeatures={
            "sinks":None,
            "toilet":None,
            "shower":None,
            "garbage can":None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["bunk room", "hallway", "queen room"],
    ),
    'queen room': Room(
        'queen room',
"Now in the Queen Room, so named for the single queen size bed, you can see thru an adjoining bathroom to the bunk room.\n\
Clearly, there are no teen age girls sharing this single bathroom, even with two sinks.\
Each side of the bed has a nightstand and matching lamp. \
The single dresser has a mirror centered above it and a closet to its left\n",
        archFeatures={
            "bed":None,
            "nightstand":None,
            "dresser":None,
            "closet":None,
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["bathroom", "hallway"],
    ),
    'master room':  Room(
        'master room',
"Now this is a master bedrom!.\n\
It's almost impossible to resist that king size bed with all those pillows and the down comforter. \
The bed is flanked by two night stands with matching lamps perched on top. A phone sits on the right side nightstand.\n\
A TV hangs above a dresser on the wall opposite the bed. To the left of the dresser is a closet.\n",
        inventory=["secret key"],
        archFeatures={
            "bed":None,
            "nightstands":None,
            "dresser":None,
            "closet":None,
            "phone":"secret key",
        },
        actions={
            "move"  : move,        
            "search" : search,
            "stop"   : stop,            
        },
        adjacentRooms=["hallway"],
    ),
}
    
def asker(keys):
    print("\n",keys)
    answer=input("\n Enter a choice from menu above or 'stop': ")
    while answer not in keys and answer != "stop":
        print("\n#####################################\n")
        print("# Sorry, that is not a valid choice #")
        print("\n#####################################\n")
        print(keys)
        answer=input("\nEnter a choice from menu above or 'stop': ")
        print("\n")
    return answer
                   
def main():
    print('Welcome to the Candy House.\n\n\
So named by the neighborhod children due t rumors of a hidden candy room. \n\
Begin by finding the hidden house key and enter the house.\n\
Then see if you can find and access the rumored Candy Room. \n\
    Good Luck.\n\n')
    
    # begin game
    room=rooms["porch"]
    answer=None
    original_room=None

    while True:
        if original_room != room:
            original_room = room
            print(room.description)
        answer = asker(list(room.actions.keys()))
        functionToCall = room.actions[answer]
        if answer == "move" :
            room=functionToCall(room)
        else:
            functionToCall(room)
            
# Create an object instance with initial state    
if __name__ == '__main__':
    main ()