# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Me")
define faye = Character("Faye")
define ethan = Character("Ethan")

# The game starts here.

label start:

    scene bg room

    show eileen happy

    #This is the Revenge Porn Storyline - CURRENTLY UNDER PROGRESS
    # TODO - Complete Revenge Porn Storyline
    # TODO - Add Faye, Ethan and player character images
    # TODO - Add Choices

    "You're currently at work and on your break. You decide to scroll through your social media for a bit before you have to go back..."

    "Whilst you're scrolling, you see that your friend, Faye has been tagged in some explicit photos..."

    "That look very much like them."

    "You look at the person who posted the images and find that they have been posted by their ex-partner, Ethan - what do you think you should do?"

    menu:

        "Contact them and let them know what's happened":
            jump contactFaye

        "Report the photos and continue scrolling":
            jump reportPhotos

        "Ignore it, it's between Faye and Ethan":
            jump ignoreImages

    label contactFaye:
        player "Hey Faye, I was just wondering if you had seen the photos Ethan's posted?"

        faye "Hey, no - what photos?"

        player "Ethan's posted some photos of you, that I assume are meant to be private?"

        faye "..."

        faye "When you say private, what do you mean? I don't understand..."

        player "Well, there's some of you in your underwear, some you're fully nude in. I wasn't sure if you knew about these photos or not?"

        "A deafining silence begins to build as you wait for Faye to respond. She comes back to the phone, breathing shakily - trying to make sense of what's just happened."

        faye "I-I told him to delete them when we broke up, w-why would he do this?"

        "You're struggling to find the right words to say, you truly don't know why Ethan would do this. They had broken up amicably only a few months ago..."

        player "Once you add a story, pictures, and music, you can release it to the world!"


    #This is the end of the road :)

    # This ends the game.

    return
