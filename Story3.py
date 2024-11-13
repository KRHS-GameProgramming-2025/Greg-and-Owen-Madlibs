from Getters import*

def Story3(debug = False):
    if debug: print("Story3 Function")


    print("\n")
    Myname1 = getMyname("What is your name, warrior? ", debug)
    Monster1 = getMonster("Enter a monster |choice: dragon. ", debug)
    Weapon1 = getWeapon("Pick a weapon |choices: Long Sword, Big Sword, Bow, Hammer, Microphone. ", debug)
    
    
    
    out = "\n"
    out += " Wake up, warrior. The king is waiting."
