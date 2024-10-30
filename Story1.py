from Getters import*

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    
    print("\n")
    friendName1 = getWord("Enter a friend's name: ", debug)
    sport1 = getSport("Enter a sport |choices: soccer, basketball, tennis. Choose all options related to basketball would be cool: ", debug)
    person1 = getPerson("Enter a person |choices: Jonkler, Batman, Tim, Ryan Goesling, Donald Duck: ", debug)
    person2 = getPerson2("Enter another person |choices: Kobe Bryant, Elon Musk, Ronaldo: ", debug)
    music1 = getMusic1("Enter a music: |choices: Basketball Music, Alphabet, C++: ", debug)
    tactics1 = getTactics1("Select tactic: |choice1: Have the ball, choice2: Give the ball to " + friendName1 + ". Please enter the number. ", debug)
    greet1 = getGreet1("Say something bad to your opponent! :D | choices: ggs, roast him. ", debug)
    
    if greet1 == "ggs":
        reaction1 = "happy"
        
    elif greet1 == "roast him":
        reaction1 = "mad"
    
    
    
    
    
    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += ", were out playing " + sport1
    out += ". Suddenly, " + person1 + " came to us."
    out += " 'What's up man.' " + person1 + " said, while his theme is playing in the background."
    out += " 'OH MY GOD! YOU'RE " + person1 + "!!' " + friendName1 + " said."
    out += " 'I know, this is crazy.' Said the big " + person1 + "."
    
    
    if person1 == "Ryan Goesling":
            out += " 'I drive, want a ride?' " + person1 + " added."
    if person1 == "Donald Duck":
            out += " 'I invite you to my DD (Donald Duck) party.' " + person1 + " said, with a lot of excitement💀"
    if person1 == "Jonkler":
            out += " 'Why---So---Serious??'🔥😀🔥 " + person1 + " laughed loudly."
    if person1 == "Tim":
            out += " 'a^2 + b^2 = c^2.'🤓 " + person1 + " said suddenly."
    if person1 == "Batman":
            out += " 'I'm Batman.' " + person1 + " said in a Batman voice."
    
            
    out += " 'And this is?' " + friendName1 + " said to " + person2
    out += ". 'Hey!' " + person2 + " said. 'I'm " + person2 + ".'"
    out += " It turned out that " + person2 + " is a friend of " + person1 + ". They came here to do some sports."
    
    if person2 == "Kobe Bryant":
         out += " 'Do you want to play ｂａｓｋｅｔｂａｌｌ with us?' " + person2 + " spoke."
    if person2 != "Kobe Bryant":
         out += " 'Can we join you guys?' Said " + person1
        
         
    out += " 'Emmmm, okay...'" + "said " + friendName1 
    out += ". 'Yooo, there's someone battling!' Our competition caught quite a lot of attention, and they put on some music. It is a song called..." + music1 + ","
    
    
    if music1 == "Basketball Music":
        out += " a song made out of footsteps and basketball bouncing sounds. Which is fire dammmnnn🔥🔥🔥"
    else:
        out += " a popular song. Which is cool."
    
        
    if tactics1 == "1":
        out += " During the game, I kept the ball the whole time. We scored some points due to my crazy shots. We won and it was a good game for me. Therefore..."
    elif tactics1 == "2":
        out += "  I passed the ball to " + friendName1 + " pretty much the whole match, and god he sucks at " + sport1 + "." + " We got cooked. Therefore... "
    else:
        print("!!!!! BAD OPTION !!!!!, tactics1")
    
    
    if greet1 == "ggs":
        out += " 'Good game man.' " + " I said. "
    elif greet1 == "roast him":
        out += " *Censored* " + " I said to " + person2 + ". 'WTH DON'T SAY THAT MAN' 😭😭😭 yelled " + friendName1 + ". "
    else:
        print("!!!!! BAD OPTION !!!!!, greet1")
    
    
    if reaction1 == "happy":
        out += " 'GGs man!' Said " + person2 + ". 'See you later!' We had a great time."
    
    
    if reaction1 == "mad":
        out += person2 + " is mad as hell...He yelled: " + " '⚡🗲🔥👹闪电旋风劈🔥🗲⚡！！！！'" + " He ran towards us. 'NAH WHY HE SPEAkING CHINESE!!???'😭😭😭 " + friendName1 + " screamed and we fleed as fast as posible"
    
    return out
