import random
import time
import discord
 
botID = 7  # <------ change this to your BOT ID
 
 
def setup():
    # greetings = ["hello", "hi there", ]
    result = "Welcome to Adventure game bot. A text based open world RPG. You will be able " \
             "to move around zones, collect items and fight monsters. \n" \
             "Controls:\n" \
             "Move North - north \n" \
             "Move South - south \n" \
             "Move East - east \n" \
             "Move West - west \n" \
             "Use Axe - use axe \n" \
             "Use Sword - use sword "
    return result
 
 
# End of  method setup
 
 
def overheard(message, user):
    global mapChoice, command
    global playerMap
    global player1
    global goblin
    global state
 
    reply = ""
    # players current position
    x = player1.positionX
    y = player1.positionY
 
    print(mapChoice[y][x])
    position = 0
 
    movement = message.upper()
 
    if state == 0:
        previousX = x
        previousY = y
 
        # Working out movement
        if movement == "NORTH":
            reply = reply + ("Going North")
            y = y - 1
            player1.positionY = y
 
        if movement == "SOUTH":
            y = y + 1
            player1.positionY = y
 
        if movement == "EAST":
            x = x + 1
            player1.positionX = x
 
        if movement == "WEST":
            x = x - 1
            player1.positionX = x
 
        # display current map
        if movement == "MAP":
            print("Displaying Map")
            stringMap = ""
            for x in range(0, 8):
                for y in range(0, 9):
                    stringMap += playerMap[x][y]
                    stringMap += ' , '
                stringMap += '\n'
            return stringMap
 
        # Set position
        position = mapChoice[y][x]
        playerMap[y][x] = "X"
        #Different spaces on map
        if position == "0":
            reply += "You cannot go any further"
            x = previousX
            y = previousY
            position = mapChoice[y][x]
            return "You cannot go any further"
 
        if position == ".":
            print("You are in an empty field")
            return "You are in an empty field"
 
        if position == "1":
            state = 1
            print("You enter a dark forest and get attacked by a goblin")
            return "You enter a dark forest and get attacked by a goblin"
 
        if position == "2":
            state = 3
            return "You come across a river with a bridge. On the bridge is an orc"
 
        if position == "3":
            hasKey = False
 
            for item in player1.inventory:
                if item.title == "Key":
                    hasKey = True
 
            if hasKey == False:
                x = previousX
                y = previousY
                position = mapChoice[y][x]
                return "There is a large iron door but you do not have a key to open it. You go back to your previous " \
                       "space"
            else:
                return "You find a large iron door and open it using a key"
 
        if position == "4":
            player1.inventory.append(sword)
            return "You find an old ruined house. Inside it is a sword"
 
        if position == "5":
            player1.inventory.append(key)
            return "You come across an old chest. You open the chest to find a key inside"
 
        if position == "6":
            hasSword = False
 
            for item in player1.inventory:
                if item.title == "sword":
                    hasSword = True
 
            if hasSword == False:
                x = previousX
                y = previousY
                position = mapChoice[y][x]
                return "You come across a dragon it can only be killed using a sword. It chases you back to the " \
                       "previous zone "
            else:
                state = 5
                return "You come across a dragon that can only be killed using a sword"
 
        if position == "7":
            state = 4
            print("You enter a dark forest and get attacked by a skeleton")
            return "You enter a dark forest and get attacked by a skeleton"
 
        if position == "8":
            state = 6
            return "You enter a graveyard and get attacked by a ghoul"
 
        if position == "9":
            state = 7
            return "While walking down the road a bandit jumps out and attacks you"
 
        if position == "10":
            state = 8
            return "You enter a crypt and inside it is a ghost that attacks you"
 
        command = message
        print(command)
        # if state == 2:
        # if "STOP" in command:
        # going = False
 
        if "HOLDING" in command:
            result = ""
            for it in heldstuff:
                result = result + it.describe()
 
            return result
 
    if state == 2:
        if "USE" in command:
            for it in heldstuff:
                print("#try use " + it.title)
                if it.title in command:
                    print("#found " + it.title)
                    return (it.action())
    #making items work in spaces
    if state == 1:
        if movement == "USE AXE":
            if position == '1':
                return "There is no enemy around"
            else:
                state = 0
                outcome = goblin.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Axe"
 
    if state == 3:
        if movement == "USE AXE":
            if position == '2':
                return "There is no enemy around"
            else:
                state = 0
                outcome = orc.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Axe"
 
    if state == 4:
        if movement == "USE AXE":
            if position == '7':
                return "There is no enemy around"
            else:
                state = 0
                outcome = skeleton.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Axe"
    #for space 6
    if state == 5:
        if movement == "USE SWORD":
            if position == '6':
                return "There is no enemy around"
            else:
                state = 0
                outcome = dragon.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Sword"
 
    if state == 6:
        if movement == "USE AXE":
            if position == '8':
                return "There is no enemy around"
            else:
                state = 0
                outcome = ghoul.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Axe"
 
    if state == 7:
        if movement == "USE AXE":
            if position == '9':
                return "There is no enemy around"
            else:
                state = 0
                outcome = bandit.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Axe"
 
    if state == 8:
        if movement == "USE AXE":
            if position == '10':
                return "There is no enemy around"
            else:
                state = 0
                outcome = ghost.damage()
                return outcome
        # return reply
        return "North, South, East, West, Map, Use Axe"
 
 
def overheardOld(message, user):
    command = message
    print(command)
    if "stop" in command:
        going = False
 
    if "holding" in command:
        result = ""
        for it in heldstuff:
            result = result + it.describe()
 
        return result
 
    if "use" in command:
        for it in heldstuff:
            print("#try use " + it.title)
            if it.title in command:
                print("#found " + it.title)
                return (it.action())
 
    return "North, South, East, West, Map"
 
 
# END of  method overheard
 
class Thing:
    def __init__(self):
        self.title = "Thing"
        self.description = "A thing you know stuff"
 
    def use(self):
        return "nothing happens"
 
    def describe(self):
        return self.description
 
 
# player class
class Player:
    def __init__(self):
        self.positionX = 0
        self.positionY = 3
        self.inventory = []
 
    def getPosition(self):
        return self.positionX, self.positionY
 
    def describe(self):
        return self.inventory
 
 
# enemy class
class Enemy:
    def __init__(self):
        self.title = "goblin"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the goblin"
        if self.health < 0:
            return "The goblin is still dead"
        return "You hit and damage the goblin for 5 health"
 
 
class Enemy2:
    def __init__(self):
        self.title = "orc"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the orc"
        if self.health < 0:
            return "The orc is still dead"
        return "You hit and damage the orc for 5 health"
 
 
class Enemy3:
    def __init__(self):
        self.title = "skeleton"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the skeleton"
        if self.health < 0:
            return "The skeleton is still dead"
        return "You hit and damage the skeleton for 5 health"
 
 
class Enemy4:
    def __init__(self):
        self.title = "ghoul"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the ghoul"
        if self.health < 0:
            return "The ghoul is still dead"
        return "You hit and damage the ghoul for 5 health"
 
 
class Enemy5:
    def __init__(self):
        self.title = "bandit"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the bandit"
        if self.health < 0:
            return "The bandit is still dead"
        return "You hit and damage the bandit for 5 health"
 
 
class Enemy6:
    def __init__(self):
        self.title = "ghost"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the ghost"
        if self.health < 0:
            return "The ghost is still dead"
        return "You hit and damage the ghost for 5 health"
 
 
class Boss:
    def __init__(self):
        self.title = "dragon"
        self.health = 10
 
    def damage(self):
        # if "use axe" or "use sword":
        self.health -= 5
        if self.health == 0:
            return "You killed the dragon"
        if self.health < 0:
            return "The dragon is still dead"
        return "You hit and damage the dragon for 5 health"
 
 
# end of class
# do this now code starts
nothing = Thing()
print(nothing.describe())
anotherthing = Thing()
print(nothing.describe())  # second thing
 
 
class Book(Thing):
    def __init__(self):
        super().__init__()  # call Things init
        self.title = "Game Tutorial"
        self.contents = "The game is controlled using text commands.\n Move North - North \n Move South - South \n"
 
        # Move East  - East \
        # Move West - West \
        # View Map - Map \
        # View Inventory - holding \
        # Use Axe - use axe \
        # Use Sword - use sword" \
 
    def use(self):
        response = "you open the book and read it"
        return response + self.title + ". " + self.contents
 
    def describe(self):
        return "a book titled " + self.title + ","
 
 
book = Book()
print(book.use())
 
 
class Axe:
    def __init__(self):
        self.title = "axe"
        self.sharpness = 10
 
    def use(self):
        self.sharpness -= 1
        return "you swing the axe it makes a wooshing sound."
 
    def describe(self):
        if self.sharpness > 5:
            return " a sharp axe,"
        else:
            return "A blunt ax"
 
    def action(self):
        return "you swing the axe it makes a wooshing sound."
 
#use for door
class Key:
    def __init__(self):
        self.title = "Key"
        self.description = " a key,"
 
    def use(self):
        return "you use the key"
 
    def describe(self):
        return self.description
 
#use for space 6
class Sword:
    def __init__(self):
        self.title = "sword"
        self.sharpness = 10
 
    def use(self):
        self.sharpness -= 1
        return "you swing the sword it makes a swoosh sound."
 
    def describe(self):
        if self.sharpness > 5:
            return " a sharp sword,"
        else:
            return "A blunt sword"
 
    def action(self):
        return "you swing the sword it makes a swoosh sound."
 
 
# class objects
ghost = Enemy6()
bandit = Enemy5()
ghoul = Enemy4()
dragon = Boss()
skeleton = Enemy3()
orc = Enemy2()
goblin = Enemy()
player1 = Player()
ax = Axe()
book = Book()
key = Key()
sword = Sword()
 
heldstuff = [book, ax, key, sword]
 
# map
worldMap = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", ".", "4", ".", ".", "5", ".", ".", "0"],
            ["0", "1", ".", "7", ".", ".", "9", ".", "0"],
            ["0", ".", "5", ".", "3", ".", ".", "6", "E"],
            ["0", ".", ".", ".", ".", "4", ".", ".", "0"],
            ["0", ".", "10", ".", "5", ".", "8", ".", "0"],
            ["0", "2", ".", "4", ".", ".", ".", ".", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]
 
# map player can see
playerMap = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["S", ".", ".", ".", ".", ".", ".", ".", "E"],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
 
 
# Displaying the map
def displayMap(maps):
    for x in range(0, 8):
        print(maps[x])
 
 
# selecting a map
mapChoice = worldMap
 
displayMap(playerMap)
 
# initialising the players position
position = mapChoice[0][0]
 
# set game state 0 is moving, 1 is fighting
state = 0
 
 
def main(mapChoice, playerMap, position):
    # players starting position
    x = 3
    y = 3
 
    print(mapChoice[y][x])
    position = 0
    while position != "E":
 
        previousX = x
        previousY = y
 
        movement = input("North,South,East,West,Map").upper()
 
        if movement == "NORTH":
            print("Going North")
            y = y - 1
 
        if movement == "SOUTH":
            y = y + 1
 
        if movement == "EAST":
            x = x + 1
 
        if movement == "WEST":
            x = x - 1
 
        if movement == "MAP":
            print("Displaying Map")
            displayMap(playerMap)
 
        position = mapChoice[y][x]
        playerMap[y][x] = "X"
 
        if position == "0":
            print("You cannot go any further")
            x = previousX
            y = previousY
            position = mapChoice[y][x]
 
        if position == ".":
            print("You are in an empty field")
 
 
# main(mapChoice, playerMap, position)
 
 
#####INGORE EVERYTHING BELOW FOR NOW ################
 
client = discord.Client()
botChannel = "bot" + str(botID)
 
 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! <')
    # print out serve name and id
    for guild in client.guilds:
        print("Server/Guild", guild.name, guild.id)
        # print out the members on this server.
        for member in guild.members:
            print("Member", member)
 
    time.sleep(3)
 
    for guildServer in client.guilds:
        chn = discord.utils.get(guildServer.text_channels, name=botChannel)
        print(f'{botChannel} found ', chn)
        message = setup()  # "I have arrived on " + botChannel
        if not (chn is None):
            await chn.send(content=message)
 
 
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
 
 
@client.event
async def on_message(message):
    print('***TELLS', message.author.name, client.user.name)
    if message.author == client.user:
        return
    if message.author.name in client.user.name:
        return
    if message.channel.name != botChannel:
        return
 
    if "CodeWrangleBot" in message.author.name or "CodeWranglingBot" in message.author.name:
        return
 
    print("** OK ", message.author.name, client.user.name)
 
    response = overheard(message.content, message.author.name)  # "I hear what you say"
    await message.channel.send(response)
 
 
Tokens = ['',  # bot 2                ADD BOT TOKEN HERE
          '',  # bot 3
          '',  # work
          '',  # work
          '',  # work
          '',  # work
          '',  # work
          '',  # work
          '',  # work
          '']  # working
 
TOKEN = Tokens[botID % len(Tokens)]
print(TOKEN, botID % len(Tokens))
 
DISCORD_GUILD = 'Codewrangling'
client.run(TOKEN)