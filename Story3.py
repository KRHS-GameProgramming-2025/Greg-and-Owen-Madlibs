from Getters import*

def Story3(debug = False):
    if debug: print("Story3 Function")


    print("\n")
    Myname1 = getMyname("What is your name, warrior? ", debug)
    Monster1 = getMonster("Enter a monster |choice: dragon. ", debug)
    Weapon1 = getWeapon("Pick a weapon |choices: Long Sword, Hammer, Microphone. ", debug)
    Potion1 = getPotion("Choose a potion |choices: Strength, Speed. ", debug) 
    Teammate1 = getTeammate("Find someone to partner up |choices: Tank, Copyman. Pick copyman pls. ", debug)
    Dodge1 = getDodge("Dodge the monster's attack |choices: 1.Do a Barrel Roll 2.Do a 360. Pick the number. ", debug)
    Song1 = getSong("Pick a song to celebrate your victory. |choices: 1. Thick of it---KSI 2. Pick 1 3. Pick 1. ", debug)
    
    out = "\n"
    out += "    'Wake up, warrior. The king is waiting.' I woke up in a luxurious room...This is really weird. I followed the servant to a large door. "
    out += "Creak...! The servant opened the door, and there, I saw a fatas---a king sitting on the throne. 'Ho Ho Ho, Ryan Goesling...The world sav---*whisper*'king, the name is " + Myname1 + ". "
    out += "Also the santa laugh is dumb.' ' Damn don't be so mean brother, my bad.' whispered back the king. These guys are terrible bruh I wanna go home. 'Back to business.' the servant cleared his throat and said. "
    out += "'" + Myname1 + ", our kingdom is in danger. There is a " + Monster1 + " destroying our public restrooms, this is intolerable. I know we're rushing you but we need to hurry. ' "
    out += "Though I have no idea why are the public restrooms so important, I decieded to help them. Definitely not because of dollars.                                                    After some consider, I picked a " + Weapon1 + " as my weapon. "
    out += "Just in case I got into a serious situation, I also took a " + Potion1 + " potion to help. After that, it's time for me to find a teammate that's willing to fight the " + Monster1 + " with me. "
    out += "The perfect place to search for teammates is the bar, where every soldier will go. I left the castle and headed the bar in a town nearby. "
    out += "                                                                                                                     While I'm walking, let me explain this. I was in Mr. Spooner's class before I woke up, I remember I clicked into...a handsome guy's project, the coding is amazing ngl, I will definitely give him a 100 if I'm the teacher💯✨✨ "
    out += "So, I'm in a country called Aberica🦅, thought it's a setting reffering to China cause the king looks like the Great wall of China but ok. " 
    out += "                                                                                                                  As I opened the door, I hear the clear sound of glasses clinks and chatters. Looking around the room I can see different people, some are strong some are small some doesn't even look like human. "
    out += "I kept waiting for a perfect person to show up, and there, I found it. The " + Teammate1 + " that just came in. "
    
        
    if Teammate1 == "tank":
        out += "It 's a tank. Yup, a T80 from the USSR to be specific. This thing is actually living which is crazy. "
    
    if Teammate1 == "copyman":
        out += "He can 100% copy anyone's attack, I deeply trust him that he can copy the dragon's attack and destroy the target! His name is Jason btw. "
    
    
    out += "                                                  Since I got my teammate, it's time to hunt the dragon. With " + Teammate1 + "'s help, I lowkey believe it's gonna be alrigh---It's not. "
    out += "When I first see the dragon, I was shocked because of how big this thing is. I held my " + Weapon1 + " tightly, I had to fight, there's no escape. "
    out += "Though I was sweating so badly, I still have hope...because I'm Diamand 1. I ran towards the dragon before it saw me and attacked it. "
    
    if Weapon1 == "Long Sword":
        out += "I succesfully damaged the dragon's skin."
        
    if Weapon1 == "Hammer":
        out += "Well well well...I have no idea what a 5 inch hammer could do, why did you pick this anyways bro. "
        
    if Weapon1 == "Microphone":
        out += "I pulled my mic out, and started singing. What the hell is wrong with me. "
        
    out += "The " + Monster1 + " thinks that I'm flirting with it and got really mad. Heat and light energy gathered around it's mouth, and a giant fireball shoots towards me. "
    
    if Dodge1 == "1":
        out += "I did a barrel roll. And suprisingly the fireball didn't hit me. "
        
    if Dodge1 == "2":
        out += "I hit a 360, it's so damn cool man😎 "
        
    out += "The fire ball hit " + Teammate1 + " instead of me. I don't know how but somehow the fireball didn't hurt him. I survived the fireball attack, but I couldn't dodge the next EMP attack from the dragon.  "
    out += "私はライアンゴズリング、あなたのドライバーです、よろしくお願いいたします。 As you can see the EMP attack changed my keyboard input to Japanese, I didn't know the dragon is this strong! "
    out += "Because this is a TBS game, it is our turn to attack now. I drank my " + Potion1 + " and attacked the dragon again. "
    out += "With the " + Potion1 + " potion's help, I was able to deal more damage to the " + Monster1 + ". "
    out += Teammate1 + "! I yelled, rizz the dragon's gyat! "
    
    if Teammate1 == "tank":
        out += "T80 loaded and fired a HEATFS, the damage it dealt is crazy, the " + Monster1 + " was injured badly and it fled." 
   
    if Teammate1 == "copyman":
        out += "'You arrogant swine, how DARE you tried to attack me, the COPYMAN??!!!💀 Your foolish blarney will be annihilated by my unplesent denouement!' "
        out += "The copyman hit a fire pose and started screaming. 'FEAR ME YOU FOOL, YOU'VE REACHED THE TOP OF MY ANGER, AND I WILL DEMOLISH YOU WITH YOUR OWN ATTACK!!' "
        out += "'...Fireball, SAME POWER!!!' The mysterious magic around the " + Teammate1 + " started glowing. 'SAME ENERGY!!!!!' The fireball growed bigger and bigger, the orange light is so strong it made my eyes hurt."
        out += "'GET HIM JASON!!' I yelled. 'KILL THAT DRAGON!!!' Jason heard me, he laughed. 'WE WILL SAVE OUR PUBLIC RESTROOM YOU NASTY LIZARD, SAME TARGET!!!!!!!!!!!!!!!!!!!!!!!!!! "
        out += "........? What the Fu-----I got hit with the biden blast. It's Joever."
        
    if Teammate1 == "tank":
        out += " The dragon is no more destroying our public restrooms now, we had a wonderful party after we went back to the kingdom. "   
    
    if Teammate1 == "copyman":
        out += "                       I passed out after the friendly fire. However, we won. Jason told me the Biden Blast scared the dragon away, and we succesfully protected the restrooms. As the game credits show up, Thick of it started playing in the background. "
        out += " We did it. We defeated the dragon! Not in a cool way though. 'HOHOHO!! I knew you can save our country!' the King and the servant showed up. "
        out += " 'We really apperciate that. Our skibidi toilets are safe!' Brain rot ahh country get me outta here. "
    
   
    
    
    return out
