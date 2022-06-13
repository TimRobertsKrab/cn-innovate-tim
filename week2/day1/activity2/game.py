# need to import your class from the other file
from character import Character
# instantiate your object from your Hero class


batman = Character("Bruce Wayne","Batman")
batman.set_power("rich")
batman.set_weakness("remembering parent's deaths")
print(batman)

print()
iron_man = Character("ToNy StaRK","Iron Man")
iron_man.set_power("high tech suit")
iron_man.set_weakness("EMP")
print(iron_man)

print()

captain_america = Character("Steve Rogers","Captain America")
captain_america.set_power("super strength")
captain_america.set_weakness("communism")
print(captain_america)
