import discord
from PyLyrics import*


client = discord.Client()

#for y in char:
#                if y==x:
#                    wordlist.append(j)
#               else:
#                    wordlist.clear()
#                j +=1
#            i +=1    

def get_lyrics():
    lyricspart1 = ("Somebody once told me the world is gonna roll me \n"
    "I ain't the sharpest tool in the shed \n"
    "She was looking kind of dumb with her finger and her thumb \n"
    "In the shape of an L on her forehead \n"
    "Well the years start coming and they don't stop coming \n"
    "Fed to the rules and I hit the ground running \n"
    "Didn't make sense not to live for fun \n"
    "Your brain gets smart but your head gets dumb \n"
    "So much to do, so much to see \n"
    "So what's wrong with taking the back streets? \n"
    "You'll never know if you don't go \n"
    "You'll never shine if you don't glow \n"
    "Hey now, you're an all-star, get your game on, go play \n"
    "Hey now, you're a rock star, get the show on, get paid \n"
    "And all that glitters is gold \n"
    "Only shooting stars break the mold \n"
    "It's a cool place and they say it gets colder \n"
    "You're bundled up now, wait till you get older \n"
    "But the meteor men beg to differ \n"
    "Judging by the hole in the satellite picture \n"
    "The ice we skate is getting pretty thin \n"
    "The water's getting warm so you might as well swim \n"
    "My world's on fire, how about yours? \n"
    "That's the way I like it and I never get bored \n")
    lyricspart2 = ("Hey now, you're an all-star, get your game on, go play \n"
    "Hey now, you're a rock star, get the show on, get paid \n"
    "All that glitters is gold \n"
    "Only shooting stars break the mold \n"
    "Hey now, you're an all-star, get your game on, go play \n"
    "Hey now, you're a rock star, get the show, on get paid \n"
    "And all that glitters is gold \n"
    "Only shooting stars \n"
    "Somebody once asked could I spare some change for gas? \n"
    "I need to get myself away from this place \n"
    "I said yep what a concept \n"
    "I could use a little fuel myself \n"
    "And we could all use a little change \n"
    "Well, the years start coming and they don't stop coming \n"
    "Fed to the rules and I hit the ground running \n"
    "Didn't make sense not to live for fun \n"
    "Your brain gets smart but your head gets dumb \n"
    "So much to do, so much to see \n"
    "So what's wrong with taking the back streets? \n"
    "You'll never know if you don't go (go!) \n"
    "You'll never shine if you don't glow \n"
    "Hey now, you're an all-star, get your game on, go play \n"
    "Hey now, you're a rock star, get the show on, get paid \n"
    "And all that glitters is gold \n"
    "Only shooting stars break the mold \n"
    "And all that glitters is gold \n"
    "Only shooting stars break the mold \n")
    lyrics = [lyricspart1, lyricspart2]

    return lyrics

@client.event
async def on_message(message):
    length = len(message.content.split())
    if message.author == client.user:
        return

    message.content = message.content.casefold()
    if message.content.startswith('somebody once'):
        msg = 'told me'.format(message)
        await client.send_message(message.channel, msg)
        # x in y = position. check position in lyrics and print next z words

    if message.content.startswith('!somebody'):
        
        msg = get_lyrics()[0]
        await client.send_message(message.channel, msg)
        msg = get_lyrics()[1]
        await client.send_message(message.channel, msg)

    if message.content in lyrics.casefold():
        if find_str(message.content):
            return
            
            
        
    
   
    

    def find_str(char):
        i=0;
        j=0;
        wordlist = []
        char.split()
        if len(char) > 1:
            lyrics = split_lyrics()
            for x in lyrics:
                if char[0] == x:
                    wordlist.append(x)
                i+=1
    
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



    

client.run('NDg0MzQxMjQ5MDM4MzUyMzg0.Dmgt-A.0VYP4DWBM3x0hrRURS7TonMFpYU')
