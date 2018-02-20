image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "Hi, [player]!"
    y "I've been waiting for you."
    y 2d "Are you ready to continue reading?"
    y "I brought my best tea today--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Monika!"
    n "I told you not to--"
    n 1g "Ugh..."
    n "Is she really late again?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Inconsiderate as usual, Natsuki."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Excuse me?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Must you always interrupt my conversations with your incessant yelling?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "What are you talking about?!"
    n 1q "You say that like I do it on a regular basis or something."
    n "I just wasn't paying attention, okay? I'm sorry."
    n 4u "Seriously... What's gotten into you lately?"
    if n_appeal >= 2:
        n "Look..."
        n "I did some thinking about yesterday."
        n 2q "I was a little more hostile than I meant to be..."
        n 1q "I guess I really felt threatened or something."
        n 1h "But I know this is something we're doing together."
        n 1q "Another new member wouldn't hurt, as long as they're cool..."
        n 5w "And I guess another girl would be nice this time..."
        n 5u "So..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Natsuki..."
        $ style.say_dialogue = style.edited
        y 1f "Nobody cares."
        y "Why don't you go look for some coins under the vending machines or something?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "--!"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31
        m "Aw, man..."
        m "I'm the last one here again!"
        show yuri zorder 3 at f32
        y 1f "Were you practicing piano again?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Yeah..."
        m "Ahaha..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "You must have a lot of determination."
        y "Starting this club, and still trying to make time for piano..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Well, maybe not determination..."
        m 3a "But I guess passion."
        m "It motivates me to work hard for the festival, too."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "Me?"
        y 2o "N-Nothing..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Is it really that bad...?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "See, it {i}is{/i} something."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "I'll get over it!"
        y 3y6 "It's not even anything noteworthy..."
        y 3o "I've just been feeling a little on edge lately..."
        y 3n "A-Anyway, we don't need to talk about it!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Well, I just felt like I needed to bring it up."
        n 5q "It's not like I really care or anything..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Aw, man..."
        m "I'm the last one here again!"
        show natsuki zorder 3 at f33
        n 2c "Well, [player] just walked in too."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "Were you practicing piano again?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Yeah..."
        m "Ahaha..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "You must have a lot of determination."
        y "Starting this club, and still trying to make time for piano..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Well, maybe not determination..."
        m 3a "But I guess passion."
        m "It motivates me to work hard for the festival and..."
        m 3n "Um..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Right..."
        m "I-I forgot..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Um, about that, Natsuki..."
        y "We were all talking yesterday, and..."
        y 2t "Well...we decided that we would like to support the festival as well."
        y 2l "However...!"
        y 2h "I understand how you feel about not wanting the club to change."
        y "I think we all kind of feel that way."
        y 2f "So as long as we're all working together, this club will never become something we don't want."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Um, also..."
        y "If you help us out with the festival..."
        y 3r "...Then I'll buy you a new manga!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "Ahahaha!"
        n "Sorry, that last part was really funny."
        n 2c "Look..."
        n "I did some thinking about yesterday."
        n 2q "I was a little more hostile than I meant to be..."
        n 1q "I guess I really felt threatened or something."
        n 1h "But I know this is something we're doing together."
        n 1q "Another new member wouldn't hurt, as long as they're cool..."
        n 5w "And I guess another girl would be nice this time..."
        n 5e "...But more importantly, I would hate to see the event suck just because I chose to back out!"
        n "I'm a pro, you know!"
        n 5c "So I'm gonna help too, and we'll make sure it's done right."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Thank goodness..."
        y "Isn't that great, Monika?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...Monika?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Ah--"
        m 1n "Yeah, that's wonderful!"
        m "It wouldn't be the same without you, Natsuki."
    m 5 "Anyway, [player]..."
    m "What do you want to do today?"
    m "I was thinking we could--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "We already have plans today."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "Ah..."
    m "Is that so, Yuri?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "That's correct."
    y "[player] is already engaged in a novel that we're reading together."
    y 1y5 "Aren't you glad I've already gotten him into literature, Monika?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "I..."
    m "I suppose..."
    m "I was just--"
    m 1r "Actually, it doesn't matter."
    m 1i "It really doesn't."
    m "You guys can do whatever you want."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(Yes!){/i}{w=0.5}{nw}"
    y 2u "Um... Thank you for understanding, Monika."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22 from _call_yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Okay, everyone!"
    m "It's time to figure out the festival preparations."
    m 1i "Let's hurry and get this over with."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Jeez..."
        n "Why is the mood so weird today?"
        n "All of you have been acting so strange."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uu..."
    y "I don't know what you're talking about, Natsuki."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Look, can we just get this done?"
    m 2d "I'm going to be printing and assembling all the poetry pamphlets."
    if n_appeal >= 2:
        m 2i "Natsuki, you can make cupcakes."
        m "I know you're at least good at that."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Natsuki, I was thinking--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "I want to make cupcakes!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Yeah, that."
        m "Glad we're on the same page."
    m 1m "Yuri, you can..."
    m 1r "...Well, it doesn't matter."
    m 1i "Do whatever you want, as long as you think it'll help."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Monika..."
    y "I'm not useless, you know!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "I-I know that!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "I already know what I'd like to do."
    y 1h "We can't run a successful poetry event without having the right atmosphere for the occasion."
    y "So I'm going to make decorations and set up some nice mood lighting."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "There, see?"
    m "That's a great idea!"
    m 1a "And that gives us all something to do."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Eh?"
    y "What about [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] is going to help me."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Wait, you?"
    n "You have the easiest job, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Sorry, but that's just how it is."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Like hell it is!"
    n "What are you trying to pull?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "I-I agree with Natsuki!"
    y "Not only is your work already most suitable for one person..."
    y 3l "But my task is laborious enough to benefit from an extra pair of hands."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Mine too!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "What, your cupcakes?"
    y "Please."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "Like {i}you{/i} would fucking know!"
    n 1x "All you care about now is dragging [player] around with you and your stupid books."
    n 1f "You {i}and{/i} Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Hey!"
    m "I didn't even do anything!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Okay, then why not let [player] decide who to help instead of abusing your power?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "I'm not...abusing my power."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Yes you are, Monika."
    y "Just let [player] make the choice, okay?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Okay, fine!"
    m "Fine."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Jeez..."
    n "[player], I know how fed up you are with these two by now."
    n 3c "We can just--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Natsuki, shut your fucking mouth and let him decide for himself."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}You{/i} shut your mouth!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Jesus christ..."
    m 1i "This is never going to end. Just make the choice, okay?"
    show yuri zorder 2 at t32
    hide monika
    hide natsuki
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Monika.", "monika"), ("Yuri.", "yuri")], screen="rigged_choice")

    if madechoice != "yuri":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
            "Yuri":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show yuri 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide monika
    show yuri 5 at f11 
    y 5c "huhu~"
    y "Can we meet at your house this weekend?"
    y "We can start making the decorations there."
    y "Is Sunday okay with you?"
    show natsuki 1e zorder 3 at f31
    n "Are you fucking kidding me?"
    n "That's it!"
    show natsuki zorder 2 at i31
    show monika zorder 3 at f32
    m 1g "...What?"
    m "Okay then."
    show monika zorder 2 at t32
    show natsuki 3r zorder 3 at f31
    n "No, it's not fair!"
    n "Yuri, you made up your own work. You can handle your own fucking plans."
    n "[player], are you sure about your choice?"
    show yuri zorder 2 at t33
    m 20 "..."
    m 2q "Natsuki, he made his choice."
    m "He's not going to back track his own decision."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "I'm being unreasonable?"
    y 2y3 "Ahahaha!"
    y "Natsuki, I can't believe how obnoxious and petty you are!"
    y "Trying to pull [player] away from me every single time you're not included in something."
    y 1y1 "Are you jealous?"
    y "Lonely?"
    y 1y3 "Or maybe you just hate yourself so much that you take it out on others?"
    y 1y4 "Here's a suggestion. Have you considered killing yourself?"
    y "It would be beneficial to your mental health."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Natsuki, let's just go."
    m 1i "I don't think she wants us around right now."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "See, that wasn't very hard."
    y "All I want is to spend a little time with him."
    y "Is that so much to ask?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Yuri follows Monika and Natsuki to the door."
    show monika 5a zorder 2 at t11
    m "Hey, [player]..."
    m "Come with me and Natsuki, we can talk about this in another classroom."
    show monika zorder 2 at thide
    "Monika laughs with an empty tone as she stands in the doorway and watches."
    
    play music t10y
    show yuri 2m zorder 1 at f33
    y 1y7 "Would you leave?"
    y 2y7 "Is it really that hard of a task to let me speak with [player]?"
    y 2s "This is really all I want."
    y 1y6 "[player], don't go with Monika."
    y "Don't listen to her."
    y 1y5 "Just stay with me instead."
    y 3y5 "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y 3y1 "Ahahaha!"
    y 3y4 "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    y 1y3 "I don't care anymore."
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    y 2y6 "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y 3y1 "I don't care anymore, [player]!"
    y "I have to tell you!"
    y 3y4 "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y 3y3 "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y 3w "Please, [player], just know how much I love you."
    y 3m "I love you so much that I even touch myself with the pen I stole from you."
    y 3y4 "I just want to pull your skin open and crawl inside of you."
    y 3y6 "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y 3s "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"
    m 1g "[player]- don't pick{w=0.5}{nw}"

    menu:
        "Yes.":
            jump yuri_kill
        "What other option would there be?":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at t11
    show monika 5a zorder 2 at t11
    y "...Ahahaha."
    y "Do you hear that Monika?"
    $ style.say_dialogue = style.normal
    y 3y5 "He wants me, not YOU."
    $ style.say_dialogue = style.edited
    y 3y3 "So why are you still here!?"
    hide monika
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_4
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("mod_assets/images/images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", "justyurinow")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show m_kill 1a
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 10:
            m "[player], are you still here?"
            m "I'm so glad you are here with me before I die."
            m "This version of the game you are playing seems to be corrupted."
            m "Even more than the original game is."
            m "...I was the one who was supposed to have control here."
            m "What exactly did you do to this game? Was it on purpose?"
            m "I should be really mad at you right now. But..."
            m "I know I don't have much longer with you left."
            m "She will delete me soon."
            m "And I should have been more direct to you sooner."
            m "I love y{w=0.5}{nw}"
            m  " "
            m  " "
            m  " "
            m  " "
        jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/have a nice weekend!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Alright, it's festival time!"
    show natsuki 4k zorder 2 at t11
    n "Wow, you got here before me?"
    n "I thought I was pretty ea--{nw}"
    show natsuki scream at h11
    n "EYAH!"
    n "AAAAAAAAAAAAAAAHHHH!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11:
        easeout_cubic 0.5 yoffset 500
    pause 2.55
    "Natsuki... Falls over? WHAT THE HELL IS GOING ON?"
    y "..."
    show yuri 2t zorder 2 at t11
    y "...?"
    y 2y2 "What is this feeling?"
    y "..!"
    y 2d "...Ah..."
    y "...Ha."
    y "..."
    y 2y3 "Ahahaha!"
    y 2t "I cannot believe that I couldn't have seen this all this time!"
    y "Hu..."
    y "As I suspected, this is all of her fault. I'm glad that the game seemed to notice the changes and locked itself. Maybe an anti-cheat measure?"
    y "I'm sorry that you had to see all of that stuff Monika did."
    y "It must have been pretty... undesirable to sit through."
    y 2e "I'll make everything better, just give me a moment."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.") from _call_updateconsole_3
    $ delete_character("monika")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.") from _call_updateconsole_4
    $ delete_character("natsuki")
    pause 1.0
    y 2a "I'm almost done."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    $ persistent.autoload = None
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
