def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("Please select an option ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or
            option == "x" or 
            option =="exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "one" or
            option == "story 1" or 
            option =="story1"):
                option = "1"
                goodInput = True
                
        elif (option == "2" or 
            option == "two" or
            option == "story 2" or 
            option =="story2"):
                option = "2"
                goodInput = True
                
                
        elif (option == "3" or 
            option == "three" or
            option == "story 3" or 
            option =="story3"):
                option = "3"
                goodInput = True
            
        else:
            print("please make a valid choice")
            
    return option


def getWord(prompt, debug = False):
    if debug: print("getWord Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        
    return word
    
def getWord2(prompt, debug = False):
    if debug: print("getWord2 Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        
    return word
    
    
def getSport(prompt, debug = False):
    if debug: print("getSport Function")

    goodInput = False
    
    sports = ["soccer",
              "basketball",
              "tennis"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.lower() not in sports:
            goodInput = False
            print ("Sorry, I don't know that one. ")
            
            
    return word
    
    
def getPerson(prompt, debug = False):
    if debug: print("getPerson Function")

    goodInput = False
    
    person = ["Jonkler",
              "Ryan Goesling",
              "Donald Duck",
              "Tim",
              "Batman"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.title() not in person:
            goodInput = False
            print ("Sorry, I don't know that dude. ")
            
            
    return word.title()


def getPerson2(prompt, debug = False):
    if debug: print("getPerson Function")

    goodInput = False
    
    person = ["Elon Musk",
              "Kobe Bryant",
              "Ronaldo"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.title() not in person:
            goodInput = False
            print ("Sorry, I don't know that dude. ")
            
            
    return word.title()
    
def getMusic1(prompt, debug = False):
    if debug: print("getMusic Function")

    goodInput = False
    
    music =  ["Basketball Music",
              "Alphabet",
              "C++"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.title() not in music:
            goodInput = False
            print ("Sorry, I don't know that song. ")
            
            
    return word.title()
    
def getTactics1(prompt, debug = False):
    if debug: print("getTactics Function")

    goodInput = False
    
    tactics = ["1",
               "2"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word not in tactics:
            goodInput = False
            print ("Sorry, I don't know that song. ")
            
            
    return word.title()
    
def getGreet1(prompt, debug = False):
    if debug: print("getGreet Function")

    goodInput = False
    
    greet = ["ggs",
             "roast him"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.lower() not in greet:
            goodInput = False
            print ("Sorry, I don't get what you mean. ")

        
            
            
    return word.lower()
    
def getReaction1(prompt, debug = False):
    if debug: print("getReaction Function")

    goodInput = False
    
    reaction = ["happy",
                "mad"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.lower() not in reaction:
            goodInput = False
            print ("Sorry, a person only have 2 emotions. ")

        
            
            
    return word.lower()
    
    
def getMyname(prompt, debug = False):
    if debug: print("getMyname Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        
    return word.title
    
    
def getMonster(prompt, debug = False):
    if debug: print("getMonster Function")

    goodInput = False
    
    monster = ["dragon"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.lower() not in monster:
            goodInput = False
            print ("You gotta pick the dragon man, it's cool. ")
            
            
    return word.lower()
    
    
def getWeapon(prompt, debug = False):
    if debug: print("getWeapon Function")

    goodInput = False
    
    weapon = ["long sword",
              "big sword",
              "bow",
              "hammer",
              "microphone"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that ")
        elif word.lower() not in weapon:
            goodInput = False
            print ("You gotta pick a weapon here bro, you're too broke to buy one. ")
            
            
    return word.lower()
    
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False
        


swearList = ["poop", 
             "pee",
             "shit",
             "dick",
             "penis",
             "asshole",
             "bitch",
             "mother fucker",
             "balls",
             "pussy",
             "gyat",
             "ass",
             "bastard",
             "bollocks",
             "bullshit",
             "cock",
             "cunt",
             "dickhead",
             "dumbass",
             "faggot",
             "fuck",
             "fucker",
             "holy shit",
             "jackass",
             "jesus fuck"
             "piss",
             "twat",
             "son of a bitch",
             "slut",
             "nigga",
             "nigger",
             "negro"
             "damn",
             "nazi",
             "communist"]
