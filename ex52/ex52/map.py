import sys

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        if name == "death":
            exit(1)

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire rew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container. There's a keypad lock on the box
and you need the code to get the bomb out. If you get the code
wrong 10 times then the lock closes forever and you can't get the
bomb. The code is 3 digits.
""")

the_bridge = Room("The Bridge",
"""
You burst onto the Bridge with the neutron destruct bomb
under you arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")

escape_pod = Room("Escape Pod", """You rush through th eship desperatly trying to make it to
the escape pod before the whole ship explodes. It seems like
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods, and
nom need to pick one to take. Some of them could be damaged
but you don't have time to look. There's 3 pods, which one
do you take?
""")

the_end_winner = Room("The End",
"""
Congratulation, you won!
""")

the_end_loser = Room("The End",
"""
Damn, you failed!
""")

escape_pod.add_paths({'2': the_end_winner, '*': the_end_loser})

generic_death = Room("death", "You died")

the_bridge.add_paths({'throw the bomb': generic_death, 'slowly place the bomb': escape_pod})

laser_weapon_armory.addpaths({
    '0132': the_bridge,
    '*': generic_death})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
    })

START = central_corridor
