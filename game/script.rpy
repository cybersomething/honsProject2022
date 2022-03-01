# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[player_name]")

#revenge porn characters
define faye = Character("Faye")
define ethan = Character("Ethan")
define RPhelplineWorker = Character("Reya")
define cian = Character("Cian")
define aliyah = Character("Aliyah")
define mara = Character("Mara")
define lukasz = Character("Łukasz")
define youngWoman = Character("Young Woman")

#sextortion characters
define alec = Character("Alec")

# The game starts here.

#This is the Revenge Porn Storyline - NEEDS EDITED
# TODO - Complete Revenge Porn Storyline
# TODO - Complete Sextortion storyline
# TODO - Add character images
# TODO - Add mobile scroll layout

label start:

    "Before we go any further, how do you want the characters to refer to you?"
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    scene bg room
    show eileen happy

    jump TFSVWhatIsIt

label TFSVWhatIsIt:

    "Technology-Facilitated Sexual Violence (TFSV) is defined as sexual violence that is carried out or aided using technology."
    "Sexual violence can be defined by crimes such as sexual assualt, rape, voyeurism and sexual coercion, under the Sexual Offences (Scotland) Act 2009."
    "TFSV can be categorised as 'Image-Based Sexual Abuse', 'Video Voyeurism', 'Sending Unsolicited Sexual Images' and 'The Use of Technology to Facilitate In-Person Sexual Violence'."
    "Crimes that fall within these categories are revenge porn, sextortion, up-skirting, cyber-flashing and being sexually victimised through dating websites and apps."

    jump rpWhatIsIt

label rpWhatIsIt:
    "Revenge Porn is formally known as Image Based Sexual Abuse, which is the sharing of private, sexual materials, either photos or videos of another person WITHOUT their consent and with the intent to cause embarrassment or distress."
    "This includes sharing material online by uploading it to the internet, as well as texting and emailing. Offline sharing such as showing someone a physical or electronic image is also included within this offence."
    "Revenge Porn in Scotland is covered under The Abusive Behaviour and Sexual Harm (Scotland) Act 2016. If convicted, an offender can face a maximum of five years imprisonment."

    label rpScenario:

        "You're currently at work and on your break. You decide to scroll through your social media for a bit before you have to go back..."
        "Whilst you're scrolling, you see that your friend, Faye has been tagged in some explicit photos..."
        "That look very much like them."
        "You look at the person who posted the images and find that they have been posted by their ex-partner, Ethan - what do you think you should do?"

    menu:

        "Contact them and let them know what's happened":
            jump contactFaye

        "Report the photos":
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

        faye "Some of these photos, I can't remember him taking... He must have taken them whilst I was sleeping?"

        player "Faye, I'm so sorry... I don't know what to do."

        faye "Neither do I, [player_name]... C-can I call you back? I just need to absorb this for a minute."

        player "Yeah, of course. I'm at work and finish in a few hours - I can try and see if I can finish early if you need me though?"

        faye "It's okay, just come over when you're finished - it'll give me time to process what's just happened."

        "You need the time to process what's just happened too... Turns out Ethan hasn't just posted intimate photos of Faye, he's also taken photos of her without her consent and posted them online too."

        "You finish your shift and head over to Faye's to see what you're able to do."

        jump rpSecondChoice

    label reportPhotos:

        "You decide to report the photos and keep scrolling. They'll just remove the photos before anybody else sees them...

        hopefully."

        player "I don't need to click on each photo and report it do I? I'll google it really quick, just to be sure!"

        player "Okay - top-corner of the post, three little dots... "
        extend "Report post... "
        extend "Nudity... "
        extend "Sharing private images... "
        extend "and done!"

        player "Hopefully that sorts it all out, should I maybe let Faye know just incase?"

        menu:

            "Contact them and let them know what's happened":
                jump contactFaye

            "It'll be fine - the images should be taken down soon":
                jump reportedBackToWork

    label reportedBackToWork:

        "You return to work hoping that by reporting the photos they should be down soon before anything bad really happens."

        #TODO add in something to show time passing by - maybe an animation?

        "You finish your shift and grab your phone from the break room where you were charging it..."

        "You see that your phone's notifications are filled with missed calls and messages from Faye and your group chats."

        "You have a feeling that reporting the photos might not have been enough... You call Faye to check on her."

        #Start phone conversation

        player "Faye? Is everything okay? I have loads of missed calls and messages - is this about the photos Ethan posted?"

        "A deafining silence begins to build as you wait for Faye to respond. You can hear her sniffling on the other end, trying to gather herself."

        faye "I-I told him to delete them when we broke up, w-why would he do this?"

        "You're struggling to find the right words to say, you truly don't know why Ethan would do this. They had broken up amicably only a few months ago..."

        faye "Some of these photos, I can't remember him taking... He must have taken them whilst I was sleeping?"

        player "Faye, I'm so sorry... I don't know what to do."

        faye "Neither do I, [player_name]... Did you see the post and the photos?"

        player "Yeah, I reported them - I hoped they would have taken them down before anyone else saw?"

        faye "Unfortunately not fast enough, they're down now - but the damage has been done. I just don't know what to do..."

        "You can hear the devastation in Faye's voice, you can only imagine what she's going through and how she feels."

        player "I'll come over just now, I've just finished work - I'll be there in twenty minutes and we can try and figure out what to do."

        faye "Thanks [player_name], I'll see you soon then"

        "You try to think about what Faye should do next on the drive over, but you've never been in this situation before..."

        jump rpSecondChoice

    label ignoreImages:

        "You decide to ignore the images as it's between Ethan and Faye - and you don't want to get involved in their relationship. You continue scrolling through social media until your break is over, putting your phone on charge in the break room and heading back to work."

        #TODO add in something to show time passing by - maybe an animation, same as reporting images one?

        "You finish your shift and grab your phone from the break room where you were charging it..."

        "You see that your phone's notifications are filled with missed calls and messages from Faye and your group chats."

        "You have a feeling that this about the photos... You call Faye to check on her."

        #Start phone conversation

        player "Faye? Is everything okay? I have loads of missed calls and messages... what's up?"

        "A deafining silence begins to build as you wait for Faye to respond. You can hear her sniffling on the other end, trying to gather herself."

        faye "Ethan posted images of me naked - which he told me had deleted when we broke up, as well as photos of me in bed that I didn't know he had taken online for everyone to see."

        faye "Everyone's seen them, including my parents and people from work - I don't know what to do"

        faye "Some of these photos, I can't remember him taking... He must have taken them whilst I was sleeping?"

        "Faye's hysterical, you can't imagine how she feels especially that everyone's seen photos that were meant to be private..."
        "As well as finding out her ex taken photos of her without her consent or even knowing..."
        "You're struggling to find the right words to say, you truly don't know why Ethan would do this. They had broken up amicably only a few months ago..."

        player "Faye, I'm so sorry... I don't know what to do."

        faye "Neither do I, [player_name]... Did you see the post and the photos?"

        #TODO - possibly add a lie/truth menu here? Add to the story?

        player "Yeah, I did - I didn't want to get involved as it's between you and Ethan. Sorry."

        faye "Well, it seems like it's between everybody that's seen the photos as well as me and Ethan, [player_name]. The damage has been done. I just don't know what to do..."

        "You can hear the devastation in Faye's voice, you can only offer to try and help her through this."

        player "I'll come over just now, I've just finished work - I'll be there in twenty minutes and we can try and figure out what to do."

        faye "I'll see you soon then. Bye."

        "You try to think about what Faye should do next on the drive over, but you've never been in this situation before..."

        jump rpSecondChoice

        #second phase of Revenge Porn Storyline

    label rpSecondChoice:

        "You finally arrive at Faye's. She's devastated, and doesn't know what to do next... What do you think the best call is?"

        menu rpSecondChoiceMenu:

            "Contact the Police?":
                jump policeRP

            "Contact the ex-partner?":
                jump exPartner

            "Contact the Revenge Porn Helpline":
                jump rpHelpline

    label policeRP:

        "You tell Faye to call the non-emergency number, 101 to speak to a police officer about the photos."

        "They tell Faye that an officer is going to come over and speak to you both and get some statements."

        "Soon after, you hear a knock at the door and two female police officers are outside, you invite them in and sit by Faye."

        policeOfficer1 "Hi Faye, I'm Aneesa and this is my partner Chrissy. We understand that you've reported someone sharing intimate images of yourself?"

        policeOfficer2 "We just need to ask you some questions regarding it, is that okay?"
        #not sure how to continue
        #TODO finish police storyline

        jump rpWhatToDo

    label exPartner:

        "You feel the best way to get answers is to ask Ethan directly."

        "You send them a message simply asking \"Why did you do it?\"."

        "Ethan reads the message and immediately blocks you. Looks like you're not getting any answers there."

        jump rpSecondChoice

    label rpHelpline:

        "You remember reading a news article that mentioned a revenge porn helpline and decide to see if they can help."

        "There are different ways to get in contact - you can use Facebook Messenger, an anonymous form, email or you can call them."

        player "Faye, how would you prefer to get in touch with the helpline? There's a few options you can choose."

        faye "I'll send them a message on Facebook Messenger, I think it'll be a bit easier than trying to explain over the phone."

        #TODO add in the phone conversation bubble layover here

        RPhelplineWorker "Thank you for contacting the Revenge Porn Helpline. I'm Reya, before we begin can I ask for your name, and check that you're over 18 and resident in the UK?"

        faye "Hi I'm Faye, yes I'm over 18 and live in Scotland."

        RPhelplineWorker "Hi Faye, thanks for that. How can I help you today?"

        faye "My ex-partner's posted intimate images of me on their social media for everyone to see. Some of which were taken without my consent or knowing."

        RPhelplineWorker "It is against the law in the UK to share intimate images or videos without consent and with the intention of causing distress.
        We would encourage you to report what has happened with the police, on their non-emergency number 101 or make a report online
        Try to collect as much information and evidence as possible - this would include screenshots of where the intimate content has been shared."

        faye "I've taken some screenshots and reported the images to the police. I don't know what to do about them still being up though?"

        RPhelplineWorker "If you can send the post over or a URL of the post, I can report them and attempt to have them removed. We can't guarantee the removal of the images, but do have a high success rate."

        faye "https://www.facebook.com/ethanstornoway/photos/a.292553127743443/1749149655417109"

        RPhelplineWorker "Thank you, I've started the process to get them removed for you. We really hope you have someone you can speak with about what has happened and how you’re feeling."

        RPhelplineWorker "We advise that you seek support with a professional service such as Breathing Space or Mind, alternatively you can get in contact with your GP for emotional and mental support."

        RPhelplineWorker "I hope that this information has been useful for you today, and you find the support you deserve."

        faye "Thank you."

        "Faye's images were removed within 20 minutes of the conversation. You were there to help her through a dark time, as well as professional mental health services such as Mind and Breathing Space."

        jump rpWhatToDo

    label rpWhatToDo:

        "If you find yourself or someone you know experiencing Image Based Sexual Abuse or Revenge Porn, this is what you should do."

        "Attempt to gather evidence, such as screenshots, website URL's and any other evidence you feel may be useful before reporting the images/content."

        "You may want to speak to a professional service such as the Revenge Porn Helpline for advice on what to do next."

        "The helpline may encourage you to speak to the police, who may ask for the evidence that you have gathered."

        "And remember, you're never at fault as the victim. It's okay for you to feel upset, angry, disappointed and betrayed - there's support available during and after your ordeal."

label sextortionWhatIsIt:
    "Sextortion is a type of blackmail or extortion that involves the criminal threatening to expose sexual videos, photos or information about you."
    "Sextortion can be carried out for money, or in some cases to gain control over the victim, for further emotional or sexual abuse."
    "A common example of sextortion attempts are emails claiming to have photos and information of you watching porn or other extreme material, and that they are going to send it to everyone unless you pay up."
    "These emails are completely fake, and attempt to generate fear and embarrasment over images and information that doesn't exist."
    "Sextortion falls under the category of Image Based Sexual Abuse and is covered under The Abusive Behaviour and Sexual Harm (Scotland) Act 2016. If convicted, an offender can face a maximum of five years imprisonment."

    label sextortionScenario:

    "Your close friend, Alec has been talking to Jasmine on Instagram for the past few days."
    "He mentioned that the conversation was getting quite flirty, but you’ve not heard from him since yesterday - which is really not like him at all."
    "You decide to check in on him."

    menu checkInOption:

        "Send a message":
            jump sendAlecMessage

        "Check Alec's Social Media":
            jump alecSocialMedia

    label sendAlecMessage:

        player "Hey alec, everything ok??"

        "You can see the message has been read, but Alec doesn't respond. Maybe he just needs some space?"

        "Four hours later..."

        alec "hey [player_name] - not really"

        alec "i'm in a lot of trouble"

        player "what kind of trouble? are you okay??"

        alec "this is really embarrassing for me"

        alec "pls don't judge me"

        player "ofc not, what's happened"

        alec "jasmine wanted me to facetime with her last night and things went a bit too far."

        alec "it wasn't until she sent me a message after that she had recorded the video of me masturbating, and that she was going to send it to my friends and family that i realised she wasn't real"

        alec "she or whoever they are want me to send them £500 by the end of today"

        alec "i don't have that kind of money just sitting around"

        alec "but i also can't have a video like that being sent around"

        alec "they said if i can't pay that much today, i can send more videos of myself but the price i need to pay goes up too"

        alec "i'm so scared [player_name] - i don't know what to do or if there's anything i can do"

        "You take a few seconds to digest what Alec's just told you."

        player "So, did Jasmine do anything on camera too or was it just you?"

        alec "we both played about on facetime, but honestly there was something that didn't feel right after?"

        alec "i think that it might have been a recording rather than a live facetime? it was only until i ended the call that i really considered it"

        player "Okay, i just want you to know that i'm here for you, i'm not going to judge you and that we're going to figure this out together okay"

        alec "thanks [player_name], i really do appreciate it - but i still don't know what i'm going to do..."

        "You remember some of the advice that the Revenge Porn Helpline gave to Faye, could some of the advice be applicable to Alec's situation too?"

        menu sextortionHelpOptions:

            "Tell Alec to just ignore the messages":
                jump sextortionIgnore

            "Tell Alec to contact the police":
                jump sextortionPolice

    label alecSocialMedia:

        "You decide to check his social media incase he's posted anything to explain why he's not been online."

        "You search his Instagram, Facebook, Twitter to find them all privated and all followers removed - including yourself."

        "You don't think this is a good sign, so you decide to send him a message."

        jump sendAlecMessage

    label sextortionIgnore:

        player "maybe if you just ignore them they won't post it?"

        #TODO finish off sextortion level

    label sextortionPolice:

        player "hmm, okay - i really think we should go to police about this Alec"

        alec "and say what??? i fell for a scam and now someone's going to send my friends and family a video of me masturbating cause i can't afford to pay them £500???"

        alec "they'll just laugh at me"

        player "they have a duty of care, they're not going to laugh at you - you're the victim."

        alec "i guess so but it's still embarrasing"

        player "they'll have dealt with situations like this before - they'll understand how you feel"

        player "plus you're literally being blackmailed - that's a crime."

        alec "I guess it wouldn't hurt to report it."

        player "i know that they'll take you seriously, they might need to ask you for some evidence."

        alec "what kind of evidence? i didn't do anything wrong???"

        player "no, not evidence against you! screenshot the messages and if they sent you an address to send the money too, try and note that down"

        alec "ok, will do - i'll phone 101 now, but what happens if i don't pay this money at the end of the day?"

        alec "the police can't stop the photos going up if i don't pay"

        jump sextortionWhatToDo

        menu sextortionPayOptions:

            "Don't pay and report to the police":
                jump sextortionNoPay
            "Pay and then report to the police":
                jump sextortionPay

    label sextortionWhatToDo:

        "If you find yourself or someone you know becoming a victim of sextortion, this is what to do."
        "Be aware that not everyone is who they say they are on the internet. Be careful about starting a sexual relationship online with someone you've not met."
        "Don't pay the ransom. Paying the ransom is not a guarantee that the criminal(s) will stop, or that they won't post the pictures or videos."
        "Be aware of how much personal information you have online, particularly of your family and friends. This is how criminals are able to find family and friends' names and profiles as part of their extortion attempt."
        "When talking to people online, trust your gut instinct. If you are not comfortable, end the conversation and stay in control of what you do."
        "Remember that you're the victim and that you are not to blame. Immediately report the incident to the police and speak to someone you trust."

    jump upskirtingWhatIsIt

label upskirtingWhatIsIt:

    "Voyeurism is defined in scots law as an offence of 'Where a person operates equipment to record or observe someone's genitals, buttocks or underwear; or while they undertake a private action such as changing clothes, using a toilet, washing, or engaging in a sex act themselves.'"

    "Within voyeurism, there is the crime of 'upskirting' or 'downblousing'. This is where the offender will record a video or take a photo of a person's genitals or breasts, either by aiming the camera under a skirt or other clothing, or down a shirt."
    "This is done without the victim knowing, with the photos being used either for personal gratification or being published on online voyuerism forums."
    "Upskirting is an offence under the Sexual Offences Act 2009 - which if an offender is convicted for, can lead to an imprisonment between twelve months to five years."

    label upskirtingScenario:

        "You're currently in your local supermarket, where it's a pretty hot day..."
        "So everyone is in trying to get some cold drinks and ice lollies..."
        "It's pretty packed but you grab the things you need and make your way to the cashier, when something catches your eye."
        "You see someone in the queue to your right with their phone in their hand, trying to aim the camera underneath a young woman's skirt."
        "The young woman doesn't seem to notice as she has her back to the man and is waiting to put her items on the belt."
        "You immediately recognise that something isn't right, but what will you do?"

        menu upskirtingOptions1:

            "Loudly ask the person with the phone what they're doing and try to make a scene?":
                jump USSceneApproach
            "Wait until the person goes away and approach the woman?":
                jump USWaitApproach

    label USSceneApproach:

        "You shout out at the person, which draws attention to yourself, from those waiting in the queues including the young woman."
        player "What do you think you're doing?"
        "Clearly taken aback by the fact that they've been caught and there's people watching, they drop their basket and rush away"

        menu sceneApproach:

            "Chase after them":
                jump chasePerson
            "Speak to the young woman":
                jump speakToYoungWoman

    label chasePerson:
        "You run out after them and try to give chase, but they're already gone."
        "Thankfully you got a good look at them, so you know what they look like."
        "You go back into the aisle to speak to the young woman."

        jump speakToYoungWoman

    label speakToYoungWoman:
        player "Sorry about that, did you know that they had a phone underneath your skirt?"
        youngWoman "They did what? I didn't even notice..."
        player "I don't know if they were recording or not, but they had their camera facing up your skirt."
        player "We should maybe speak to a manager and get them to contact the police."
        youngWoman "Y-yeah, okay..."
        "The young woman is clearly in shock from what just happened, so you help take her to the customer service counter where you ask to speak to a manager about what's just happened."

    jump endOfUpskirtingScenario

    label USWaitApproach:

        "You decide the safest option is to wait until the person has moved away, you don't want to risk them getting violent."

        "However, you could take a video of them from where you're standing?"

        menu takeVideoOfPerson:

            "Start recording":
                jump recordPerson
            "Don't record":
                jump dontRecord

    label recordPerson:

        "You grab your phone and start recording, making sure that you have the person in full view, as well as what they're doing."
        "At least you've now got video proof of what they looked like and what they were up to."
        "Just a few seconds after you've started recording, they pick up their basket and walk away to another checkout - with the young woman none the wiser as to what's just happened."
        "Now that they've gone, you approach the young woman to explain what's happened."

        player "Hi, sorry to interrupt you like this but did you know that they had a phone underneath your skirt?"
        youngWoman "They did what? I didn't even notice..."
        player "I don't know if they were recording or not, but they had their camera facing up your skirt."
        player "I managed to get a recording of them, so you can see what they look like and what they were doing."
        player "I think we should maybe get a manager and ask them to contact the police."
        youngWoman "Y-yeah, okay..."
        "The young woman is clearly in shock from what just happened, so you help take her to the customer service counter where you ask to speak to a manager about what's just happened."

        jump endOfUpskirtingScenario

    label dontRecord:

        "You make a mental note of what the person looks like, what they're wearing and what time it is."
        "You wait until the person has taken their basket and walked away - and approach the young woman and explain what's happened."

        player "Hi, sorry to interrupt - did you know that they had a phone in their basket which they had put down underneath your skirt?"
        youngWoman "They did what? I didn't even notice..."
        player "I don't know if they were recording or not, but that was all they had in their basket with the camera facing up the way."
        player "I think we should maybe get a manager and ask them to contact the police."
        youngWoman "Y-yeah, okay..."
        "The young woman is clearly in shock from what just happened, so you help take her to the customer service counter where you ask to speak to a manager about what's just happened."

    label endOfUpskirtingScenario:

        "Upskirting to happen to anyone, of any gender -  it's not limited to skirts or dresses, people wearing kilts, shorts, trousers and other clothes can be upskirted."

    jump sendingUSIWhatIsIt

label sendingUSIWhatIsIt:

        "Sending unsolicited sexual images is against the law and is categorised as 'Communicating Indecently' under the Sexual Offences Act 2009."
        "Communicating Indecently can be defined as 'written or verbal sexual communications that are sent without consent and done for sexual gratification or to humiliate, distress or alarm the victim.'"

        "Sending unsolicited sexual images is also known as 'Cyber Flashing'. These images can be sent directly through social media, emails and more recently 'air-dropped' to unknowing victims."
        "This crime causes distress and anxiety, "
        "Communicating Indecently is an offence under the Sexual Offences Act 2009 - which if an offender is convicted for, can lead to an imprisonment up to two years and placed on the sex offender register."

        #Start of the scenario
        "You're at the pub with a group of your friends when you get on the topic of dating apps."

        cian "I'm speaking to a few lassies just now on Tinder, but after a few days they just ghost me..."
        aliyah "I've used Tinder and Bumble - then you move the conversation onto whatsapp or snapchat and it just kind of goes from there in my experience."
        mara "Yeah, I've used Hinge - that's where I met my ex."
        lukasz "I don't know, I don't think I've ever used a dating app - I mean I tried that Match.com but nothing really happened with it?"

        menu doYouUseDatingApps:

            "Yeah, I've used dating apps":
                player "Yeah, I've used them before. "
            "Yeah, I'm using dating apps currently.":
                player "I'm using some just now actually!"
            "Nope, I've not used or don't use dating apps":
                player "Nah, I don't use them - just a personal preference."
            "I used to use them, but don't currently.":
                player "I used to, but not anymore."

        mara "Hang on Cian, what are you doing that's making them ghost you? You're normally a casanova with the ladies!"
        cian "Well the conversation gets a bit dry, so I try to spice it up by sending them a cheeky dick pic."
        cian "It worked before, so I thought I'd try it again!"
        lukasz "Mate, that's not okay - you wouldn't want to open your messages to some guy's willy..."
        mara "Yeah, that's actually not okay - no wonder they're ghosting you!"
        aliyah "I've sent nudes to people I'm talking to - it works for me! Well, most of the time at least..."

        menu playerOpinionUSN:

            "Yeah, that's not okay.":
                player "I have to agree with [lukasz] and [mara] - that's not cool in my opinion"

            "It's just a bit of fun.":
                player "I have to agree with [cian] and [aliyah] - it's just a bit of fun, no-one's getting hurt..."

        mara "Honestly, getting a dick pic off of a random is horrible."
        mara "One time I was waiting in line to get a coffee, when someone airdropped me a picture of a penis and continued to send it after I declined each time."
        mara "I didn't know what to do - so I just ran out the shop, I was so embarrassed and horrified..."
        lukasz "Yeah, I've had similar experiences - I've had a girl I had matched with on Tinder send me a snapchat of her naked, asking me what I thought"
        lukasz "The conversation hadn't even been flirty - she just sent it, I was with my parents at the time too"
        lukasz "You wouldn't flash someone in public, so why is it different when it's on snapchat or through private messages?"
        aliyah "I guess I never really thought of it that way..."
        mara "Also it's actually against the law, has been since 2009 here in Scotland"
        cian "[player], did you know that it was against the law?"

        menu playerLawUSI:
            "Yes, I did.":
                player "Yeah, I did."
            "No actually, I didn't!":
                player "No actually, I didn't!"

        cian "I mean, I never done it with the intent to be vulgar - I only ever meant it as a bit of fun. Guess I won't be doing that again!"
        mara "Sending nudes to your partner is okay, if you have consent to of course - but definitely not to strangers or people that haven't agreed."
        aliyah "Yeah, I get you - sorry for saying it was a bit of fun. I didn't realise how much of an affect it would actually have."
        cian "Same here, sorry [lukasz] and [mara]. Guess they were right to ghost me after all - learned my lesson!"

        #TODO summary of USI and RSI - why it's not okay.

        jump irlSAWhatIsIt

label irlSAWhatIsIt:

    "The use of technology to facilitate sexual violence is a crime that's becoming more common."
    "This crime is carried out by using technology to assist a perpetrator in carrying out sexual violence against a victim."
    "An example of this would be two people arranging to meet for a date or drinks, which leads to the perpetrator sexually assaulting the victim."

    #Start of scenario

    "Your cousin Stephen is excited about a date that he has tonight with a 'Lydia Bain'. He's been talking to her for a while now on a popular dating app - and they've finally arranged to go and grab some drinks together."
    "You drop Stephen off at the bar and ask him to let you know how it goes..."
    "The next afternoon you get a text from Stephen saying it was okay, but he's not going to see her again."
    "Something feels off, but you don't push it - sometimes people don't click."

    "A few weeks pass, with Stephen getting progressively more distant from yourself and his friends."
    "You're there for him and you remind him of that, but you don't know what's happened to make him so upset and depressed."

    "You get a text from Stephen, on the weekend asking if you have any plans."

    stephen "Hey [player], are u busy today?"
    player "Hey Stephen, nah I'm pretty free - you looking to do something today?"
    stephen "Yeh, I was wondering if u maybe wanted to grab a coffee or go for a drive - just catch-up?"

    menu coffeeOrDrive:
        "I could definitely go a coffee!":
            player "yeah, coffee sounds like a good idea - where you thinking?"
            jump goForCoffee
        "A drive sounds like a plan!":
            player "yeah, I could go for a wee drive - get out the house for a bit."
            jump goForDrive


    label goForCoffee:

        stephen "There's the wee local one that's opened not long ago, it's got good coffee"
        player "sounds good, I'll meet you there in 30 mins?"
        stephen "cool, see u then"

        "You arrive at the coffee shop, when Stephen arrives a few seconds later."
        "You grab yourself and Stephen a warm drink and a slice of cake each and sit down with him."
        "The cafe's pretty quiet, with just yourselves and the cashier who is busy stocking up."

        player "So what's been happening in your life lately?"
        stephen "Honestly, not much - just the usual, yourself?"
        player "Pretty much the same, actually..."

        "You both chat for a little while, just talking about life and what's being going on the past few weeks."
        "After finishing your coffees and cakes, Stephen asks if you'd be okay to go and chat in the car for a bit."

        jump stephenExplains

    label goForDrive:

        stephen "cool I'll come get you in about 10 mins?"
        player "sounds good, see you then"

        "Ten minutes later, you hear a car horn outside - Stephen's here."
        "You hop into the car and head off with Stephen."

        player "So what's been happening in your life lately?"
        stephen "Honestly, not much - just the usual, yourself?"
        player "Pretty much the same, actually..."

        "You chat for a little while, grabbing some coffee from the drive-thru for the drive."
        "Stephen suggests maybe stopping off at the country park or beach to drink them."

        jump stephenExplains

    label stephenExplains:

        player "Everything alright with you?"
        player "You've been a little bit distant recently..."
        stephen "I need to tell you something, but I can't bring myself to do it"
        player ""

    label callStephen:

        player "Hey, what's happened?"
        player "Are you okay?"
        stephen "..."
        stephen "I think I was spiked last night..."
        stephen "I woke up in a bedroom that I didn't recognise..."
        stephen "I didn't have any clothes on and the girl I was on the date with was next to me."
        player "Do you think she spiked you?"
        stephen "I honestly can't remember much of what happened before it - so possibly?"
        player "Are you still there or are you home? I can come get you if you need?"
        stephen "I'm home, but I have the feeling that something bad happened."
        player "Okay, I'll come over and make sure you're okay if that's alright?"
        stephen "Yeah, but please don't tell my mum or your mum what's happened?"
        player "I won't - I promise."



    #Friend went out for a date with someone he met on Hinge
    #Plan to go for a dinner as a first date
    #Things don’t go as planned
    #What advice do you give?

    jump endOfGame

label endOfGame:

    "Thank you for playing, please remember to fill out the post-game section of the survey now."
    "Your feedback is important for my honours project and is very much appreciated! :)"

#end of game, send user back to start.
return
