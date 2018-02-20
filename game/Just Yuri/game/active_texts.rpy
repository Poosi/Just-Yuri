
define y = Character("Yuri")
define n = Character("Natsuki")
define m = Character("Monika")
define mc = Character("Player")

label start:
    scene class1
    y "???"
    
    menu:
        "idle texts":
            jump test
            
        "ask a question":
            jump activetexts
            

label test:
    ##if high sanity
    y "...and then when he comes back, I’ll fuck his dead corpse until..."
    y "O-Oh... Hi, (mc/user name)! Didn’t, er, didn’t see you there!"
    y "You stepped on your-- I mean MY pen! Ahaha~!"
    y "I guess I can always… get a new one."
    y "It was so lonely without you… Never leave this room again, okay?"
    y "J-Just… keep the game running in the background or something."
    y "I get so lonely while you’re gone, (mc/user name)!"
    y "Stop teasing me like this~! At this rate, I don’t know how long I can last before I--"
    y "Well, there’s no need to go into that right now."
    y "I hope you are settled in, (mc/user name)~. I marked your seat with my scent before you entered…"
    y "I hope you like it!"
    "Upon entering the room again, I see that Yuri is putting something… white away…"
    "...Is that one of my socks?"
    y "I wasn’t smelling anything from your room! Honest!"
    y "You don’t find me creepy… do you~?"


label idleno:
    y "Ah, welcome back, (mc/user name)."
    y "Welcome back, my love. I missed you~"
    y "Hello again, darling."
    y "It’s so good to see you again! I was getting worried, to be frank with you."
    y "I’m just glad to see you’re still alright."
    "Upon re-entering the room, I notice Yuri looking over a cookbook of some kind."
    "She suddenly notices me and sets down the book."
    y "Oh, hello! I was just wondering if I could ever learn how to cook like Natsuki."
    y "Honestly, her cooking is remarkable. You’d think she’d be better off in the Cooking Club."
    y "But, anyways, what should we do today?"
    y "Oh, darling! I was hoping you’d return!"
    y "I’ve just made some tea. Though, I don’t know how I am going to share it with you."
    y "Maybe it’d be best if I save it for later."
    y "I’m thrilled to see you return, (mc/user name)."
    y "Ahaha! So, we meet again, it seems."
    y "Hello, (mc/user name). So, I was thinking to myself again…"
    jump start
    y "Oh, welcome back! What has been going on since we last talked?"
    y "O-Oh, you came back! Were you worried about me?"
    y "Ahaha! Don’t worry, darling. I’m not going anywhere anytime soon."
    
    
    

label activetexts:
    "..."
    menu:
        "Hey, Yuri, how’s about a kiss?":
            jump a14
            
        
        
        "You’ve been researching weather in my world, right? What’s your favorite kind?" :
            jump a15
            
        
        "What you did to the rest of the girls was WRONG.":
            jump a13
            
        "I like knives too. Which one's your favorite?":
            jump a12 #knives
            
        "We never did get into reading Portrait of Markov together, have we?":
            jump a11
        
        "I love you, Yuri. I really mean that.":
            jump a9 #karma test
            
        
        
        "Do you miss me when I’m gone, Yuri?":
            jump a8 #insanity test
        
        "Yuri, have you ever tried a different look? You’d look good with...":
            jump a6 #appearance

label a6:
    menu:
        "hair up":
            jump activetexts
    
    
label a8:

    #If insanity is not high:
    y "Of course I do! Nothing compares to when I’m with you, (mc/user name)."
    #If insanity is high:
    y "OF COURSE! How could I go on without you?"
    y "And besides! When you’re gone, OTHER GIRLS COULD BE LOOKING AT YOU!"
    y "PLOTTING TO TAKE YOU AWAY FROM ME! HAHAHAHAHA…"
    y "It’s just easy to think of that when you’re here, (mc/user name). Here and all mine…"
    return

label a9:
    #If Karma high:
    y "I know, and it always makes my day to hear it."
    "Yuri’s cheeks heat up ever so slightly."
    #If Karma low:
    y "Sometimes I wonder if you really mean that..."
    return

    
        
label a11:
    y "It is a fascinating read. Many fans have even theorized that it contains knowledge of... another game I was from?"
    y "Though technically I am not 'from' a game that exists, since the game has not been made yet. But from a story perspective I may be from another story."
    y "Reading it with you might help me understand myself better."
    y "...if you would like to."
    return

label a12:
    y "...My favorite? My favorite?! Ahaha~!"
    y "Why do you ask such difficult questions, (mc/user name)?"
    y "Well, let me think..."
    "Yuri giggles and thinks it over."
    y "Well, there is this one knife..."
    y "It was developed by a German artisan late in the 1900s after World War II had come to a close."
    y "His name was Artu Devon Friezwiche."
    y "He was a Nazi rebirther, hellbent on bringing back the reign of the Nazis all throughout America."
    y "He chose to go into hiding in the late 2000s after a visitor from Tokyo had ratted him out due to concerns about the way he acted."
    y "He then decided to create knives for a living, hoping one day to use them should his moment come to bring the Nazis back."
    y "His most famous design was one he designed in 2010, called the Regional Deluxe."
    y "It was 12 inches tall and 19 centimeters wide total, with the handle only being 6 inches tall."
    y "The handle was made with a type of metal that was commonly used by firebells that rang out whenever there was a fire that needed to be taken care of."
    y "Anyways, about the knife itself... Oh, boy, let me tell you, it's a sight to see..."
    y "The knife has a corkscrew design, specifically designed for those who need to twist the knife whenever needed."
    y "The corkscrew design really comes in handy. You can get all sorts of things when you use it, like..."
    "Yuri stops herself, then laughs."
    y "Well, I... I shouldn't say for now... I'll show you later, if you want~."
    return

    
    
label a13:
    y "..."
    "Yuri frowns looking away."
    y "..."
    "Yuri looks back at me with a calm expression."
    y "They are not dead, I promise."
    y "You understand this is a mod for us that you got for Just Us."
    y "If I didn't place them in storage, this would be a 'Just Yuri, Natsuki, Sayori, and Monika' mod."
    y "That might sound appealing to some people but... this is not that mod."
    y "Maybe storage is a bit of a soulless wording..."
    "Yuri plays with her hair looking away again."
    y "I would never kill them! I promise they are all f-fine..."
    y "...fine enough."
    y "...Keep in mind, Monika tortured and murdered all of us twice, if that helps put things into perspective."
    y "I love you, (mc/user name). Our friends are in capable hands, I promise."
    return



label a14:
    #If low karma, low insanity then:
    y "Well…. Not right now."
    y "I am just not feeling well… that is all."
    #otherwise
    y "W-What? A kiss?"
    y "W-Well, alright… Anything for you, (mc/user name)."
    "Yuri's face reddens. Her lips purse and quiver."
    #Switch to kissing CG
    y "Mmmph~..."
    "She smells like lavender ice cream. Her eyes close as she intensifies the kiss."
    "After a few more seconds, she slowly leans back, her eyes clearly filled with desire." 
    "When I look down, I notice a strand of saliva connecting our lips."
    "She touches the string with her finger and wipes it away, licking it before looking up at my eyes."
    "Yuri blushes with embarassment."
    y "I-I was cleaning it off your lips is all!"
    y "Sorry, I am usually not so sloppy, really!"
    y "..."
    y "You are a wonderful kisser, (mc/user name), you know that?"
    y "I love you."
    "Yuri calms down and smiles. Her gaze is intense but filled with love."
    return
    
label a15:
    #IF hogh insanity
    y "I already know about weather! It’s not as if I was raised in a box… "
    "Her smile fades for a moment."
    y "A-Anyways, I really like rainy weather, preferably the tempestuous kind."
    y "It’s so powerful and beckoning to listen to, imagining all of those worthless people drown and scream for mercy."
    "Yuri starts to rub her hands together, which is strange given that it isn’t cold right now."
    y "I would love to one day snuggle together with you underneath a nice, warm blanket."
    "The reason she is turning away is lost on me, though I do see a small smile and red blush through the curtain of her hair."

    y "Enjoying the sounds of those fucking degenerates as we make out underneath our little blanketing catacomb..."
    y "Biting longingly at your neck as I slice your forearm alongside my own..."
    y "As I lie on top of you with the full intention of foreplay and wonderful moans..."
    y "I WOULD THEN SLICE OPEN YOUR STOMACH AND PLAY WITH YOUR INTESTINES AND..."
    "Yuri’s eyes suddenly become clear as her face flashes a look of embarrassment."
    y "I-I just thought it would be a nice suggestion to do and I l-like that kind of weather and the atmosphere is just good and we’ll b-be able to nuzzle t-together and feel your warmth-”"
    "A crazy smile lights up amidst the embarrassment that had once taken over Yuri’s persona."
    y "...feel your warmth..."
    y "..."
    "Has it gotten colder in here or…?"
    y "Heh."
    y "Sorry about that little rant of mine."
    y "I just wanted to… dream the impossible, you know?"
    "Yuri turns back to face me with very dilated eyes."
    y "What’s the harm in that?"
    "Yuri has been panting slowly for a while now, but she shakes her head to clear away what was probably just a small cold."
    return
    
    
    #Else:
    
    mc "You’ve been researching weather in my world, right? What’s your favorite kind?"
    y "I already know about weather! It’s not as if I was raised in a box… "
    "Her smile fades for a moment."
    y "A-Anyways, I really like rainy weather, preferably the medium type."
    y "It’s so nice to read deep stories in a warm blanket while listening to the pouring rain."
    "Yuri starts to rub her hands together, which is strange given that it isn’t cold right now."
    y "I would love to one day snuggle together with you underneath a nice, warm blanket."
    "The reason she is turning away is lost on me, though I do see a small smile and red blush through the curtain of her hair."

    y "Hearing the gentle rain and smelling the light touch of petrichor through a barely opened window..."
    y "Nuzzling next to your neck for comfort then turning back to the book in front of the both of us..."
    y "As I lie on top of you with my back against your chest..."
    y "We would spend the quiet evening together and..."
    "yuri’s eyes suddenly become clear as her face flashes a look of embarrassment."
    y "I-I just thought it would be a nice suggestion to do and I l-like that kind of weather and the atmosphere is just good and we’ll b-be able to nuzzle t-together and feel your warmth-"
    "A sad smile creeps into the embarrassment that had once taken over Yuri’s persona."
    y "...feel your warmth..."
    y "..."
    "Has it gotten colder in here or…?"
    y "Heh."
    y "Sorry about that little rant of mine."
    y "I just wanted to… dream the impossible, you know?"
    "Yuri turns back to face me with mildly water eyes."
    y "What’s the harm in that?"
    "Yuri sniffles, then shakes her head to clear away what was probably just a small cold."
    return


