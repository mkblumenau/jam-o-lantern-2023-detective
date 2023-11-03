# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Valerie", image="valerie_virde")
define m = Character("Marshall", image="marshall")
define h = Character("Hibiki", image="hibiki")
define nm = Character("Male newscaster", what_italic=True)
define nf = Character("Female newscaster", what_italic=True)


# Declare splash images:
image cover:
    "/images/splash/game cover.png"

image cover_text:
    "/images/splash/extraordinary detective marshall.png"

image marshall_end:
    "/images/splash/marshall end.png"

image marshall_arrested_end:
    "/images/splash/marshall arrested end.png"

image ransom_note:
    "/images/items/ransom note.png"

image remote:
    "/images/items/remote.png"

image switchblade:
    "/images/items/switchblade.png"


# Define sounds.
define audio.beaming = "/audio/beaming-mirror-1.ogg"
define audio.pageflip = "/audio/page-flip.ogg"
define audio.penclick = "/audio/pen-click.wav"
define audio.tablepound = "/audio/table-pound.ogg"
define audio.static = "/audio/tv-static.ogg"


# The game starts here.

label start:
    # Initialize variables for the game.
    default evidenceFound = []
    # This could also be done with separate boolean variables for each possible piece of evidence.
    # Also add the compassion/pressure variables for the characters.

    
    jump act1_start


label act1_start:

    #Add the TV background and music once we have them.
    scene bg room

    """
    You've seen this scene many times before.

    Static dances across the TV screen, filling your ears with an incessant buzzing.

    It seems the regular programs haven't started yet.

    Your hands twitch in anticipation. Television is a familiar comfort to you.

    You watch the news once every morning, and once every night. A little detective's habit you picked up.

    It's good to stay in the know, hm?

    Just as you start to despair over the delay, a channel list appears on the TV screen.

    What do you want to remember?
    """
    
    menu:
        # At the moment, the only one of these that's complete is DD News.
        "DD News":
            "It flips to the channel the moment you think of it."
            # The characters for this are set to say everything in italics, so we don't need to add that here.
            nm "What's up everybody, this is the Daily Downer News Channel!"
            nm "Here's your daily dose of downing for your morning commute. Looks like those stocks are just going to keep on crashing, baby!"
            nf "I hope you didn't buy a home in the past three years, because you're gonna have to sell it soon. We're in a recession!"
            nm "Oh yeah, you heard us right. While those interest rates go up up up, my money is going down, down, down."
            nf "Even our broadcasting network might have to shut down! Haha!"
            nm "I wouldn't pack your bags just yet missy! We can always rely on government bailouts eventually!"
            nf "But isn't the government in total massive crippling debt? Where will they get the billions of dollars?"
            nm "Haha, they'll just take that money away from the school systems and police departments. Like usual!"
            nf "That is so true, Brian! Well that's all for our morning report, we hope you have a dreadful day. That's DD News!"

        "USABN":
            "It flips to the channel the moment you think of it."

        "Orenji Local News":
            "It flips to the channel the moment you think of it."

        "Kartoon Network":
            "It flips to the channel the moment you think of it."

    jump act1_crimescene


label act1_crimescene:
    # scene with crime scene background, once we have that
    scene bg crimescene
    show marshall neutral at left:
        zoom 0.2
    

    """
    You step into the alleyway and glance around, shivering at the noticeable drop in temperature. The buildings on all three sides seem to loom over and close in on you, making the space feel suffocating.

    The sun hasn't risen high enough for its light to cast over the space, instead creating shadows that stretch and warp. 
    """

    m "{i}I'm surprised nothing has occurred here until now.{/i}"
    m thinking "{i}Then again, shady business could've happened here that just flew under our radar.{/i}"

    "Yellow police tape block off the far end of the alley where the covered body lay. You step under it and look around."

    default act1_alleySeen = False
    default act1_surroundingsSearched = False
    default act1_cellPhoneSearched = False


    jump act1_crimescene_menu

    #jump act2


label act1_crimescene_menu:
    # If no conditions are available, it will just bypass the menu.
    # Also, remember to edit the evidence menu in screens.rpy
    # so it has all the items that can be found as evidence,
    # either here or in other parts of the script.
    
    show marshall thinking
    menu:
        "Collected evidence can be seen within the Preferences menu."

        "Examine the dead body." if not "bodyExamination" in evidenceFound:
            """
            You search for a clean corner and carefully lift the tarp up to expose the face, making sure to not have direct contact with any of the blood.

            Underneath was a boy wearing an East Orenji High School uniform. His face is contorted in ghastly shock.
            """

            m realization "{i}Wait, is that... the Chief's son?{/i}"
            "You've seen Maximus Rismaune around at holiday parties hosted by the Chief's family, but you were never interested in interacting with him despite his importance."
            m neutral "{i}Not even the Chief himself is safe now huh?{/i}"
            m "{i}Makes sense why Detective Virde seemed off this morning.{/i}"
            "Dropping the tarp, you kneel down next to the body and lay a hand on its shoulder. It's warm to the touch and no rigor seems to be present yet."
            m thinking "{i}Time of death must be fairly recent then. Around three hours ago, maybe.{/i}"
            "You drag the trap further down to reveal more of the upper body, which is covered in deep lacerations."
            m "{i}Looks to be the work of a knife.{/i}"

            "{b}New Evidence!{/b}\nObtained: - Body Examination"
            $ evidenceFound.append("bodyExamination")

            "You replace the tarp on the body."
            jump act1_crimescene_menu

        "Look through the fallen backpack." if not "ransomNote" in evidenceFound:
            # Put the actual text here.
            """
            You tip the backpack over and peer inside. You're greeted by a mess of notebooks and folders stuffed with pieces of paper riddled with creases and smudged pencil marks.

            Underneath all of that were slices of milk bread packed in a ziplock bag. They were so stale they managed to withstand the crushing weight without so much as budging an inch.
            """

            m disgusted "{i}Kids these days can't even bother to organize a backpack.{/i}"
            m "{i}Don’t even get me started on that bread. It looks like it’s been in there for weeks.{/i}"

            """
            Looking closer, you spot a crisp and clean piece of paper poking out of a folder. It looks so out of place you were surprised you missed it the first time around.

            You reach in, careful not to disturb the intricate pile of overlapping school stationary, and grab it.
            """

            window hide dissolve
            show ransom_note with dissolve:
                xalign 0.5
                yalign 0.5
                zoom 0.5
            pause
            # put "pause 2" to wait for 2 seconds
            # instead I just set it up to wait for another click
            hide ransom_note with dissolve
            window show dissolve

            "{b}New Evidence!{/b}\nObtained: - Ransom Note"
            $ evidenceFound.append("ransomNote")

            m thinking "..."
            jump act1_crimescene_menu

        "Examine the alley floor." if not act1_alleySeen:
            $ act1_alleySeen = True
            "Dried blood stains the floor all around where the body lies."
            "You notice slightly further up the alley a large smear of blood that travels and feathers towards the back like a gruesome paint stroke."
            m thinking "{i}That kid must've struggled quite a bit before dying. What a mess…{/i}"
            jump act1_crimescene_menu

        "Search the body's surroundings." if not act1_surroundingsSearched:
            jump act1_crimescene_surroundings_search

    # This is what happens if the menu is bypassed.
    jump act1_crimescene_post_exam


label act1_crimescene_surroundings_search:
    menu:
        "Your eyes circle around the body and lock onto two items of interest sprawled on the floor next to it."

        "Scroll through the cell phone." if not act1_cellPhoneSearched:
            $ act1_cellPhoneSearched = True
            """
            You pick up the cell phone with a handkerchief and flip it open. Strangely enough, the phone is unlocked. Opened up are text conversations with a contact named 'Sister', with the most recent messages dating from last night.

            You scroll through the texts. There isn't much to note from them except for the victim's almost obsessive interest in tormenting 'some loser at school' named Hibiki, much to the sister's disinterest.
            """

        "Examine the bloody switchblade." if not "bloodySwitchblade" in evidenceFound:
            """
            You pick up the switchblade with a handkerchief and twist it around in your hand, watching as a sliver of light reflects off the sharp blade.

            Along the handle is scrawled in all caps what looks to be a name: 'Hibiki'. The handwriting is jagged, almost desperate, despite the writer's best efforts to make it look neat. 
            """

            window hide dissolve
            show switchblade with dissolve:
                xalign 0.5
                yalign 0.5
                zoom 0.4
            pause
            hide switchblade with dissolve
            window show dissolve

            "{b}New Evidence!{/b}\nObtained: - Bloody Switchblade"
            $ evidenceFound.append("bloodySwitchblade")

        "Back":
            pass
    
    # After each choice, check if both search options are complete.
    if act1_cellPhoneSearched and "bloodySwitchblade" in evidenceFound:
        $ act1_surroundingsSearched = True
    
    # Then jump back to the main menu.
    jump act1_crimescene_menu


label act1_crimescene_post_exam:
    m neutral "{i}That seems to be all the evidence I can get from here.{/i}"
    m @ thinking "{i}Hmm… My strongest lead right now would be whoever this 'Hibiki' kid is.{/i}"
    m "{i}Seems straightforward enough. Not only does he seem to have a connection to the Chief's son, but there's also a knife with his name on it at the crime scene.{/i}"
    m smile "{i}I didn't expect to determine a suspect so soon… I guess it's just my lucky day.{/i}"
    jump act2


label act2:
    "We don't have act 2 yet."

    jump act3


label act3:
    "Or act 3."

    return #I assume the game will end here. This may change.


screen bar_example(inputValue, xalignValue):
    # inputValue is the percentage that you want the bar to be full.
    frame:
        xalign xalignValue ypos 50
        xsize 500
        bar:
            value StaticValue(inputValue, 100)
 