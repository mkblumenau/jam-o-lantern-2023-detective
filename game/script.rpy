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

    
    jump act1


label act1:

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
 