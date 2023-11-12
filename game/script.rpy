# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Valerie", image="valerie_virde")
define m = Character("Marshall", image="marshall")
define h = Character("Hibiki", image="hibiki")
define r = Character("Risumane", image="risumane")
define nm = Character("Male newscaster", what_italic=True)
define nf = Character("Female newscaster", what_italic=True)
define disembodied_voice = Character("???")


# Declare splash images:
image cover:
    "/images/splash/game cover.png"

image cover_text:
    "/images/splash/extraordinary detective marshall.png"

image marshall_end:
    "/images/splash/marshall end.png"

image hibiki_arrested_end:
    "/images/splash/hibiki arrested end.png"

image jax_arrested_end:
    "/images/splash/jax arrested end.png"

image marshall_arrested_end:
    "/images/splash/marshall arrested end.png"

image valerie_point_splash:
    "images/splash/valerie point splash art.png"


# Define images used for items.
image ransom_note:
    "/images/items/ransom note.png"

image remote:
    "/images/items/remote.png"

image switchblade:
    "/images/items/switchblade.png"


# Define background images.
image crime_scene:
    "/images/backgrounds/crime scene.png"

image detective_office:
    "/images/backgrounds/detective office.png"

image interrogation_room:
    "/images/backgrounds/interrogation room.png"

image schoolyard:
    "/images/backgrounds/schoolyard.png"

image television:
    "/images/backgrounds/television.png"


# Define SFX.
define audio.beaming = "/audio/sfx/beaming-mirror-1.ogg"
define audio.pageflip = "/audio/sfx/page-flip.ogg"
define audio.penclick = "/audio/sfx/pen-click.wav"
define audio.tablepound = "/audio/sfx/table-pound.ogg"
define audio.static = "/audio/sfx/tv-static.ogg"


# Define audio.
define audio.interrogation = "/audio/music/Interrogation.wav"
define audio.menumusic = "/audio/music/Menu_Music.mp3"
define audio.normalscene = "/audio/music/Normal_Scene_Music.mp3"
define audio.waltz = "/audio/music/ Waltz 23.11.2.wav"
define audio.mystery1 = "/audio/music/Mystery 1 23.11.2.wav"
define audio.mystery2 = "/audio/music/Mystery 2 23.11.2.wav"


# The game starts here.

label start:
    # Initialize variables for the game.
    default evidenceFound = []
    # This could also be done with separate boolean variables for each possible piece of evidence.
    # Also add the compassion/pressure variables for the characters.

    
    jump act1_start


label act1_start:
    scene television
    play music static # Putting this on the music channel means that it will loop by default.

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

    default act1_kartoon_seen = False
    default act1_ddnews_seen = False
    default act1_usabn_seen = False
    default act1_oln_seen = False
    default one_show_left = True
    jump act1_tv_menu


label act1_tv_menu:   
    menu:
        # At the moment, the only one of these that's complete is DD News.
        "DD News" if not act1_ddnews_seen:
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
            $ act1_ddnews_seen = True

        "USABN" if not act1_usabn_seen:
            "It flips to the channel the moment you think of it."
            nm """
            This is USABN, the only broadcasting network bringing you the truth, and only the honest truth.

            Violent and petty crime are on the rise across the country. Last night, a group of teen delinquents in San Fontista broke into a hunting goods store, stealing over 40 knives and firearms.

            The teens have since been caught, but with the minor protection laws in this country, they're unlikely to face any substantial punishment.

            What has happened to this world? How are we going to be safe if these criminals just keep getting let loose?

            Thieves, gangsters, murderers- they're all walking in broad daylight nowadays.

            Police, politicians, all across the country! Do something already!

            Save us! Save the youth!
            """

            "The program ends. Finally."
            $ act1_usabn_seen = True

        "Orenji Local News" if not act1_oln_seen:
            "It flips to the channel the moment you think of it."
            nf "{i}Thank you for tuning in to OLN, your local news channel for everything happening in Orenji.{/i}"
            nf "{i}The vehicular manslaughter case that shocked the town three months ago still has no clear perpetrator.{/i}"
            nf "{i}We have just received a statement from Chief Rismaune of the OPD regarding the incident.{/i}"
            r "{i}Good evening, ladies and gentlemen. The OPD is still actively investigating the death of Rex Radoncic, a good soul snuffed out far too early.{/i}"
            r "{i}According to our sources, he was fatally struck by a vehicle in the outskirts of town in the early hours of the day.{/i}"
            r "{i}Our investigation team is working hard to unveil the truth behind the tragedy. We offer our heartfelt condolences to the family of the victim, and hope to finally bring this perpetrator to justice.{/i}"
            r "{i}If you have any tips related to the incident, please call…{/i}"
            "The program ends."
            $ act1_oln_seen = True


        "Kartoon Network" if not act1_kartoon_seen:
            "As hard as you try, you simply can’t imagine what shenanigans would be playing on this channel."
            $ act1_kartoon_seen = True
            jump act1_tv_menu

    # If it doesn't jump from Kartoon Network, it should go here after the choice.

    if one_show_left:
        "You have time to watch one more program. "
        "What do you want to remember?"
        $ one_show_left = False
        jump act1_tv_menu
    else:
        stop music

        "You are finished watching TV. A heavy weight burdens your shoulders."
        "Despite all of your greatest efforts, the world is still plagued with dirt and evil."
        "You think of all the innocent people close to you. "
        "How can you protect them? "
        "Your tired eyes blink at the TV screen. "

        play sound beaming
        show television with Fade(0.5, 1.0, 0.5, color="#ffffff")

        "A comforting voice rumbles from the tinny speakers."
        disembodied_voice "{i}This is a task only you can undertake.{/i}"
        disembodied_voice "{i}Cleanse the gloom that proliferates the world with your righteous justice.{/i}"
        disembodied_voice "{i}Do your best, Extraordinary Detective Marshall.{/i}"

        play sound beaming
        # <fade to white>

        jump act1_orenji_police_station

label act1_orenji_police_station:
    scene black with Fade(1.5, 0.0, 0.5)
    "{b}Orenji Police Station{/b}"

    
    play music normalscene
    show valerie_virde neutral at right:
        zoom 0.2

    v "Huh, you actually made it on time today."

    scene detective_office with Fade(0.5, 1.0, 0.5, color="#ffffff")
    show valerie_virde neutral at right:
        zoom 0.2
    show marshall neutral at left:
        zoom 0.2
    
    "The voice startles you out of your daze. Apparently you were daydreaming on your walk to work."
    m smile "Oh- good morning ma'am!"
    m laugh "Are you proud of me? Nine o'clock on the dot."
    v annoyed "Don't push your luck. This doesn't make up for the fact you were late all week."
    show marshall neutral
    menu:
        "Sorry for the trouble":
            m smile "Sorry for the trouble."
            v neutral "Just don't make it a habit, you know how uptight the Chief can get about these things."

        "My bad.":
            m neutral "My bad."
            v neutral "Just don't make it a habit, you know how uptight the Chief can get about these things."

        "Shouldn't you be at your desk?":
            m laugh "Shouldn't you be at your desk?"
            v "Watch it. I'm still your superior."
            v "Besides, I wouldn't need a smoke break this early in the morning if people came to work on time {i}consistently...{/i}."
            m "Heh, noted."

    v neutral "What’s the hold up, anyway? Late riser?"
    m laugh "Quite the opposite, actually. I tend to get carried away on my morning walks."
    m thinking "Which, I understand, is completely my fault. But I’m here now."
    v "Alright, alright. In any case, let’s move onto more pressing matters."
    v annoyed "Cases have been popping up left and right lately, so we can’t afford to have OPD’s golden boy have his head in the clouds."
    v thinking "On top of that, the Chief has been especially difficult to work with…"

    "This is what we have for now, so we're skipping ahead a little."
    jump act1_crimescene


label act1_orenji_police_station_old:
    # This was in the script previously, but it seems to have been removed.
    scene detective_office with Fade(0.5, 1.0, 0.5, color="#ffffff")
    show valerie_virde neutral at right:
        zoom 0.2
    show marshall neutral at left:
        zoom 0.2
    v  "I see someone decided to take his job seriously today."

    # <Fade into the outside of East Orenji Police Station background>

    # <Marshall neutral on the left and Detective Virde annoyed on the right>

    "The voice startles you out of your daze. You blink rapidly to reorient yourself."
    "Despite your strange daydreaming, it seems you successfully made your way to the police station."

    "Leaning on the side of the building, partly hidden by shadows, stood Detective Virde. The only thing illuminating your superior’s face is the faint glow of her cigarette. "

    hide marshall
    show marshall smile at left:
        zoom 0.2
    m "{i}Oh no… It’s never a good sign if she’s smoking this early. I might’ve pushed my luck too far this week.{/i}"

    m "{i} I should try my best not to anger her any further.{/i}"

    "You walk up to her, trying to look at ease despite the overwhelming urge to ignore her and bolt inside to the safety of your office."

    "You don’t want a longer and harsher tirade from her later on, though."

    m "Good morning ma’am!"

    v "Do you want to explain to me why this is the first time in a week you’ve been on time?"

    "unfortunately, we will not know why this is the first time he's been on time! the game will be finished eventually"


label act1_crimescene:
    
    play music normalscene
    scene crime_scene
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


label act1_crimescene_menu:
    # If no conditions are available, it will just bypass the menu.
    # Also, remember to edit the evidence menu in screens.rpy
    # so it has all the items that can be found as evidence,
    # either here or in other parts of the script.

    show marshall thinking
    menu:
        "Collected evidence can be seen within the Preferences menu."

        "Examine the dead body." if "bodyExamination" not in evidenceFound:
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
    stop music
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
 