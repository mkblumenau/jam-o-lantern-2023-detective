# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Valerie")
define m = Character("Marshall", image="marshall")

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


# The game starts here.

label start:
    # Initialize variables for the game.
    default evidenceFound = []
    # This could also be done with separate boolean variables for each possible piece of evidence.
    # Also add the compassion/pressure variables for the characters.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    "Temporary text" "The text that's in here now is just a placeholder. But if we make the text really long then we can see the effect of it on this textbox design, which may or not be as we desire."

    #This is just to test that the sprites for Marshall are displaying properly.
    show marshall annoyed at center:
        zoom 0.2

    m "I should be annoyed."

    #show m smile
    m smile "But now I smile."

    jump act1

    # This ends the game.

    return

label act1:

    scene bg room

    "Divine light except idk how to write it yet"

    #show valerie at left
    show marshall neutral at right:
        zoom 0.2

    v "I see someone decided to take his job seriously today."

    menu:
        "Address obviously pointed remark":
            m "After the thirty or so calls from you yesterday on both my cell and landline I thought it would ERROR SENTENCE NOT FINISHED"
            v "(something, I don't know what)"

        "Ignore":
            m "Good morning Detective Virde! The day's barely started and you're already taking a break?"
            v "I wouldn't need a break if I didn't have to deal with strange men at the station and chase around ace detectives like they're rookies."

    m "Strange men at the station?"

    v "As I was coming in today there was a man just standing at the front desk. Didn't move or talk at all. Creeped out the receptionist."
    m "Huh. You don't see that every day."
    v "Thought he was going to attack her so I was about to intervene when he spun around and left."
    v "Wouldn't be surprised if it was a local gang member thinking he's real funny."
    v "Maybe this will finally convince the Chief to listen to me and set up extra security measures around here."
    "She shook her head and pinched the bridge of her nose."
    v "Enough about that. This is the first time you've been on time in a week. What have you been doing? I can only give so many excuses when the Chief comes around asking for you."

    # A choice should happen here. It's not in the script yet.

    m "My apologies Detective. I've been getting carried away on my morning walks lately. I promise I won't do it again."
    v "Fine, I'll hold you to it."
    "She gave Marshall a sharp look before leaning back against the wall and drawing another puff from her cigarette. She signed, exhaling wispy gray smoke that curled around her like talons."
    v "Cases have been popping up left and right lately and now I have to deal with an ace detective with his head in the clouds. What am I going to do..."
    m "Would you please do this somewhere else? I washed this coat yesterday and it would be awful if you got ashes on it."
    v "Oh come on, a little ash on your coat won't kill you. It's not like I'm rubbing it all over you."
    "As if to demonstrate, Detective Virde waved and jabbed the smoldering end of her cigarette in that air, causing Marshall to cringe further back. "
    m "Detective, if you bring that infernal... thing anywhere closer to me I might consider going back on that promise."
    v "Hah! Alright, alright. Though if I were you I would spend more energy worrying about my cases than my appearance."
    v "Speaking of, Chief told me to let you know that a case came up this morning that is of... high priority."

    jump act2

label act2:
    "We don't have act 2 yet."

    jump act3

label act3:
    "Or act 3."

    # I used this space to test out showing bars on the screen.
    # We can tweak this later, but it gives you an idea of what
    # the cooperation meters might look like.
    "Anyway, here's a bar."
    $ barValue = 25
    show screen bar_example(barValue, 0.5)
    "Oh look, it's a bar! How nice."
    show screen bar_example(90, 0.5)
    "Fuller now."
    # Create a second version of the bar.
    show screen bar_example(30, 0) as bar2
    "Another one."
    show screen bar_example(60, 0) as bar2
    "Updating it."

screen bar_example(inputValue, xalignValue):
    # inputValue is the percentage that you want the bar to be full.
    frame:
        xalign xalignValue ypos 50
        xsize 500
        bar:
            value StaticValue(inputValue, 100)
 