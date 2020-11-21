import discord
import random
from discord.ext import commands
from random import choice


client = commands.Bot(command_prefix = "yo mama ")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('"yo mama help"'))
    print("yo mama is ready")

#Ping
@client.command()
async def ping(ctx):
    
    mama_ping = [ 
        "Yo mama so hungry, that she ate the whole supermarket in",
        "Yo mama so fast, that she ran the marathon in",
        'Yo mama so joke hungry, that she types "yomama ping" every',
        "Yo mama so obesse, that she gains 1kg every"
        "Yo mama so fat, that she fell from space to the earth in",
    ]
    
    await ctx.send(f'{random.choice(mama_ping)} **{round(client.latency * 1000)} ms**.')
    print("pinged by {message.author}")

#Help
@client.command()
async def help(ctx):
    

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    
    embed.add_field(name="info", value="Info about the bot.", inline=False)
    embed.add_field(name="invite", value="Invites yo mama to your server.", inline=False)
    embed.add_field(name="ping", value="Latency of the bot.", inline=False)
    embed.add_field(name="jokes", value="Shows list of jokes.", inline=False)
    embed.add_field(name="fun", value="Shows list of fun commands.", inline=False)
    

    await ctx.send(embed=embed)
    print("yo mama helped")

#Help jokes
@client.command()
async def jokes(ctx):
    

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    
    embed.add_field(name="random", value="Tells a RANDOM yo mama joke.", inline=False)
    embed.add_field(name="fat", value="Tells a yo mama so fat joke.", inline=False)
    embed.add_field(name="ugly", value="Tells a yo mama so ugly joke.", inline=False)
    embed.add_field(name="old", value="Tells a yo mama so old joke.", inline=False)

    
    

    await ctx.send(embed=embed)
    print("yo mama helped with jokes")

#Fun commands
@client.command()
async def fun(ctx):
    

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    
    embed.add_field(name="swag", value="Measures your swag score.", inline=False)
    embed.add_field(name="gay", value="Measures your gayness.", inline=False)
    embed.add_field(name="dick", value="Measures your pp size...", inline=False)
    embed.add_field(name="8ball", value="Answers your questions.", inline=False)
    
    

    await ctx.send(embed=embed)
    print("yo mama helped with fun commands")



#Info
@client.command(aliases=["about"])
async def info(ctx):
    

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    
    embed.add_field(name="About", value="This bot is made for entertainment purposes, and it isnt meant to offend or harrass someone. This bot is inspired by yo mama youtube channel.", inline=True)
    embed.set_image(url="https://cdn.discordapp.com/attachments/778661584054255618/778924675396927518/yomama.jpg")
    embed.add_field(name="My Twitter", value="[click here](LINK)", inline=False)
    embed.add_field(name="Yo mama bot Discord", value="[click here](LINK)")
    embed.set_footer(text="https://www.youtube.com/user/yomama")
    

    await ctx.send(embed=embed)
    print("yo mama sent yo the info")



#Invite
@client.command()
async def invite(ctx):
    
    embed = discord.Embed(
        colour = discord.Colour.orange(),
        title = "Invite me to your server!",
        description = "[Click me to invite](LINK)"
        )

    embed.set_image(url="https://cdn.discordapp.com/attachments/778661584054255618/778924675396927518/yomama.jpg")

    await ctx.send(embed=embed)
    print("yo mama invited")


#---------------------FUN COMMANDS---------------------

@client.command(aliases=["cock", "dick"])
async def _dick(ctx):
    
    dick_meter = [ "10", "9", "8", 
                  "20", "19", "18", "17", "16", "15", "14", "13", "12", "11",
                  
]
    
    await ctx.send(f'Your dick is **{random.choice(dick_meter)}cm** big.')
    print('Measured dick')




@client.command(aliases=["gay", "gayness"])
async def _gayness(ctx):
    
    gay_meter = range(0, 100)
    
    await ctx.send(f'You are **{random.choice(gay_meter)}%** gay!')
    print('Measured Swag')

@client.command()
async def uwu(ctx):
  
    
    await ctx.send(f'OWO')
    print('owo')

@client.command(aliases=["swag"])
async def _swag(ctx):
    
    swag_meter = range(0, 100)
]
    
    await ctx.send(f'Your swag score is **{random.choice(swag_meter)}/100**!')
    print('Measured Swag')

@client.command(aliases=['8ball', '8Ball', 'eightball'])
async def _8ball(ctx, *, question):
    
    ball_responses = [  "Yes",
                   "No",
                   "Probably",
                   "Maybe",
                   "That was a dumb question",
                   "I don't know",
                   "Most likely",
                   "I guess so",
                   "Ask someone else",
                   "Definitely",
                   "Nope",
                   "Lmao",
                   "Most likely",
                   "Yup"
                   ]
    
    await ctx.send(f'{random.choice(ball_responses)}')
    print('The 8ball has answered.')

#----------------Random Joke Generator----------------
    

@client.command(aliases=['random'])
async def _random(ctx):
    
    adjective = [
                        'ugly',
                        'fat',
                        'old',
                        'scary',
                        'stupid',
                        'poor',
                        'crazy',
                        'skinny',
                        'hungry',
                        'small',
                        'angry',
                        'sad',
                        'shy',
                        'sleepy',
                        'terrific',
                        'dead inside',
                        'naughty',
                        'evil',
                        'filthy',
                        'bad',
                        'bizzare',
                        'funny',

    ]

    verb = [
                        'eated',
                        'scared away',
                        "can't afford",
                        'killed',
                        'cooked',
                        'stole',
                        'destroyed',
                        'pooped out',
                        'accidentaly sitted on',
                        'shot with a gun at',
                        'threw poop at',
                        'farted at',
                        'fell on',
                        'readed a book about',
                        'became',
                        'is scared of',
                        'threw up because she saw',
                        'pooped at',
                        'got killed by',
                        'prayed to',
                        'bought',
                        'is addicted to',
                        'kissed',

    ]


    noun = [  
                         'the crows',
                         'a child',
                         'a dog',
                         'a man',
                         'a bird',
                         'an hamburger',
                         'the hamburgers',
                         'the coke',
                         'a car',
                         'a bike',
                         'a hospital',
                         'a police station',
                         'you',
                         'your parents',
                         'your mom',
                         'your dad',
                         'your sister',
                         'your brother',
                         'your family',
                         'a Walmart',
                         'a Ikea',
                         'the dogs',
                         'the cat',
                         'a cat',
                         'the cats',
                         'barrack obama',
                         'bill gates',
                         'poop',
                         'beans',
                         'bible',
                         'waffles',
                         'a cancer',
                         'diabetes',
                         'your waifu',
                         'memes',
                         'pee',
                         'pizza',
                         'weed',
                         'shrek',

    ]

    await ctx.send(f'Yo mama so {random.choice(adjective)} that she {random.choice(verb)} {random.choice(noun)}!')
    print('Told yomama a random joke')



#--------------------YO MAMA JOKES--------------------

@client.command(aliases=['sofat'])
async def fat(ctx):
    
    yomama_fat = [  
        'Yo mama is so fat that her bellybutton gets home 15 minutes before she does.',
        'Yo mama is so fat that the only exercise she gets is when she chases the ice cream truck.',
        'Yo mama is so fat that when she gets in an elevator, it has to go down.',
        'Yo mama is so fat and dumb that the only reason she opened her email was because she heard it contained spam.',
        'Yo mama is so fat that when she was diagnosed with a flesh-eating disease, the doctor gave her ten years to live.',
        'Yo mama is so fat that the National Weather Service names each one of her farts.',
        'Yo mama is so fat that she looked up cheat codes for Wii Fit.',
        "Yo mama is so fat that she sat on a dollar and squeezed a booger out George Washington's nose.",
        'Yo mama is so fat that that when she sits on the beach, Greenpeace shows up and tries to tow her back into the ocean...',
        'Yo mama is so fat that light bends around her.',
        "Yo mama is so fat that I took a picture of her last Christmas and it's still printing!",
        'Yo mama is so fat that when she sat on Wal-Mart, she lowered the prices.',
        "Yo mama so fat when she played Among Us she couldn't get through the vents.",
        'Yo mama so fat her idea of dieting is deleting the cookies from the internet cache.',
        'Yo mama so fat it took 3 years for Nationwide to get on her side.',
        "Yo mama so fat that when she fell down the stairs, I wasn't laughing but the stairs were cracking up.",
        "yo mama so fat that she doesn't need the internet - she's worldwide.",
        'yo mama so fat that when she goes on a scale, it shows her own phone number.',
        'Yo mama is so fat that when she goes to an all you can eat buffet, they have to install speed bumps.',
        'Yo mama is so fat that she went to the fair and the kids thought she was a bouncy castle.',
        'Yo mama is so fat that she stands in two time zones.',
        'Yo mama is so fat that that when I tried to drive around her I ran out of gas.',
        'Yo mama is so fat that when she fell over she rocked herself asleep trying to get up again.',
        "Yo mama is so fat that when she visited Toronto's City Hall, she was arrested for attempting to smuggle 150kg of crack into Mayor Rob Ford's office.",
        'Yo mama is so fat that Dracula got Type 2 Diabetes after biting her neck.',
        'Yo mama is so fat that when we were playing Call of Duty, I got a 20 kill streak for killing her.',
        "Yo mama is so fat that they use the elastic in her underwear for bungee jumping.",
        'Yo mama is so ugly that when she was born she was put in an incubator with tinted windows.',
        'Yo mama is so ugly that she put the Boogie Man out of business!',
        'Yo mama is so ugly that she made Barack Obama lose hope!',
        'Yo mama was such an ugly baby that her parents had to feed her with a slingshot.',
        'Yo mama is so ugly that she made an onion cry!',
        'Yo mama is so ugly that when I last saw a mouth like hers, it had a hook in it.',
        'Yo mama is so ugly that she gets 364 extra days to dress up for Halloween!',
        'Yo mama is so ugly that when she plays Mortal Kombat, Scorpion tells her to "Stay Over There!"',
        'Yo mama is so ugly that neither Jacob nor Edward want her on their team.',
        'Yo mama is so ugly that they push her face into dough to make gorilla cookies.',
        'Yo mama is so ugly that when she goes to the therapist, he makes her lie on the couch face down.',
        'Yo mama is so ugly that she gives Freddy Kreuger nightmares. ',
        'Yo mama is so ugly that when she walks in the kitchen, the rats jump on the table and start screaming.',
        'Yo mama is so ugly that if she was a scarecrow, the corn would run away.',

                   ]
    
    await ctx.send(f'{random.choice(yomama_fat)}')
    print('Told yomama fat joke')

@client.command(aliases=['sougly'])
async def ugly(ctx):
    
    yomama_ugly = [  
        'Yo mama is so ugly that she looked out the window and got arrested for mooning.',
        'Yo mama is so ugly that people go as her for Halloween.',
        'Yo mama is so ugly that she turned Medusa to stone!',
        'Yo mama is so ugly that... well... look at you!',
        'Yo mama is so ugly that when she looks in the mirror, the reflection looks back and shakes its head.',
        'Yo mama is so ugly that she makes blind children cry.',
        'Yo mama is so ugly that her shadow ran away from her.',
        'Yo mama is so ugly that her birth certificate contained an apology letter from the condom factory.',
        'Yo mama is so ugly that she tried to take a bath and the water jumped out!',
        'Yo mama is so ugly that her mom had to be drunk to breast feed her.',
        'Yo mama is so ugly that when she walks into a bank, they turn off the surveillence cameras.',
        'Yo mama is so ugly that when she was born, the doctor slapped her AND her parents!',
        "Yo mama is so ugly that she didn't get hit with the ugly stick, she got hit by the whole damn tree. ",
        'Yo mama is so ugly that she has 7 years bad luck just trying to look at herself in the mirror.',
        'Yo mama is so ugly that she practices birth control by leaving the lights on. ',
        "Yo mama is so ugly that she threw a boomerang and it wouldn't even come back.",
        "Yo mama is so ugly that she'd scare the monster out of Loch Ness.",
        'Yo mama is so ugly that her pillow cries at night.',
        'Yo mama is so ugly that people at the circus pay money not to see her.',
        'Yo mama is so ugly that when she looks in the mirror it says "viewer discretion is advised." ',
        'Yo mama is so ugly that when she moved into the projects, all her neighbors chipped in for curtains.',
        'Yo mama is so ugly that Santa pays an elf to drop off her gifts at Christmas.',
        "Yo mama is so ugly that people hang her picture in their cars so their radios don't get stolen.",
        'Yo mama is so ugly that I took her to a haunted house and she came out with a job application.',
        "Yo mama is so ugly that the FCC requires her face to be blurred when she's on TV, because of decency rules.",
        'Yo mama is so ugly that government intelligence agencies have to pixelize her face when spying on her. ',
        "Yo mama is so ugly that she's never seen herself 'cause the mirrors keep breaking.",
        'Yo mama is so ugly that it looks like someone did the stanky leg dance on her face.',
        


                   ]
    
    await ctx.send(f'{random.choice(yomama_ugly)}')
    print('Told yomama ugly joke')


@client.command(aliases=['souold'])
async def old(ctx):
    
    yomama_old = [  
        'Yo mama is so old that when she farts, dust comes out.',
        'Yo mama is so old that I told her to act her own age, and she died.',
        'Yo mama is so old that she knew Burger King while he was still a prince.',
        "Yo mama is so old that she has Adam and Eve's autographs.",
        'Yo mama is so old that she co-wrote the Ten Commandments.',
        'Yo mama is so old that her social security number is 1.',
        'Yo mama is so old that her birth certificate is written in Roman numerals.',
        'Yo mama is so old that she has an autographed bible.',
        'Yo mama is so old that her birth certificate says "expired" on it.',
        'Yo mama is so old that that when she was in school there was no history class.',
        'Yo mama is so old she remembers when the Mayans published their calendar.',
        'Yo mama is so old that she owes Fred Flintstone a food stamp.',
        'Yo mama is so old that the candles cost more than the birthday cake.',
        'Yo mama is so old that she drove a chariot to high school.',
        'Yo mama is so old that she took her drivers test on a dinosaur.',
        'Yo mama is so old that her memory is in black and white.',
        'Yo mama is so old that she sat next to Jesus in third grade.',
        "Yo mama is so old that she knew Cap'n Crunch while he was still a private.",
        'Yo mama is so old that when she was born, the Dead Sea was just getting sick.',


                   ]
    
    await ctx.send(f'{random.choice(yomama_old)}')
    print('Told yomama so old joke')











client.run("TOKEN")
