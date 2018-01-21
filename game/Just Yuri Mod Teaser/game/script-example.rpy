##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label example_chapter:
    stop music fadeout 2.0

    image monika_room = "images/cg/monika/monika_room.png"

    #This set's up the scene with a background and music
    scene monika_room
    with dissolve_scene_full
    play music t6


    #You will also want to show characters of other images
    show yuri 1 at t11 zorder 2
    mc "Yuri, I’ve been thinking..."
    mc "Why do we have to sit across from each other like this?"

    "Yuri gives a mildly confused look."
    show yuri 1n at t11 zorder 2

    y 1o "What do you mean?"
    mc "I mean, we’ve gotten pretty close…"
    mc "Maybe we can…"
    mc "Sit next to each other?"

    "The level of heat rising to Yuri’s face is enough to make me reciprocate her own blush."
    show yuri 3e2 at t11 zorder 2

    mc "I w-was just thinking... you don't have to if you don’t want to it... I'm sorry if I was going too far. "

    "Yuri shakes her head violently. What’s gotten into her?"
    show yuri 3v at t11 zorder 2

    y 3p "NO!"
    y 3q "N-no."
    y "I-I mean I’d love to but no you’re not going too far at all."
    y 1b2 "Just… let me prepare everything..."

    "All of the lights turn off."
    "Just what is Yuri planning?"
    "I can hear multiple objects shuffling across the floor, which is strange given that Yuri is only one person."

    #Switch CG to the next to Yuri in study CG.
    stop music fadeout 0.5
    scene black


    y 1b "Hi, (mc)!"

    "Yuri’s blush becomes more intense when we lock eyes."
