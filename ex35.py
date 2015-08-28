from sys import exit

prompt = ("> ")

def gold_room():
    """Make the player enter the gold_room"""
    print("This room is full of gold. How much do you take?")
    next = input(prompt)
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    """Make the player enter the bear_room"""
    print("""There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?""")
    bear_moved = False

    while True:
        next = input(prompt)
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    """Make the player enter the cthulhu's room"""
    print("""Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?""")

    next = input(prompt)

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    """Kill the player"""
    print(why, "Good job!")
    exit(0)

def start():
    """Start the game"""
    print("""You are in a dark room.
    There is a door to your right and left.
    Which one do you take?""")

    next = input(prompt)

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

 
