from Getters import*

def Story3(debug = False):
    if debug: print("Story3 Function")


    print("\n")
    Myname1 = getMyname("What is your name, warrior? ", debug)
    Monster1 = getMonster("Enter a monster |choice: dragon. ", debug)
    Weapon1 = getWeapon("Pick a weapon |choices: Long Sword, Big Sword, Bow, Hammer, Microphone. ", debug)
    Potion1 = getPotion("Choose a potion |choices: Invisibility, Strength, Speed. ", debug) 
    Teammate1 = getTeammate("Find someone to partner up |choices: Mage, Tank, COPY MAN(he's chill). ", debug)
    
    out = "\n"
    out += " 'Wake up, warrior. The king is waiting.' I woke up in a luxurious room...This is really weird. I followed the servant to a large door. "
    out += "Creak...! The servant opened the door, and there, I saw a fatas---a king sitting on the throne. 'Ho Ho Ho, Ryan Goesling...The world sav---' *whisper* 'king, the name is " + Myname1 + ". "
    out += "Also the santa laugh is dumb.' ' Damn don't be so mean brother, my bad.' whispered the king. These guys are terrible bruh I wanna go home. 'Back to the business.' servant cleared his throat and said. "
    out += "'" + Myname1 + ", our kingdom is in danger. There is a " + Monster1 + " destroying our public restrooms, this is intolerable.' "
    
    
    
    
   
    return out
