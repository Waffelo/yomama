import discord
import random
import os


from random import choice
from discord.ext import commands


client = commands.Bot(command_prefix = 'OwO ')
client.run('TOKEN')

@client.event
async def on_ready():
    print("bot is ready")

#Ping command

@client.command()
async def ping(ctx):
    await ctx.send(f'**pong!** *{round(client.latency * 1000)}ms*')
    

#Hug

@client.command(pass_context=True)
async def hug(ctx, *, user:discord.Member):
    

    await ctx.send(f'{ctx.author.mention} hugged {user.mention}')
    print("Hugged")

 

#8BALL Command

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
                   ]
    
    await ctx.send(f'{random.choice(ball_responses)}')
    print('The 8ball has answered.')

#Idea rating

@client.command(aliases=['idea', 'Idea'])
async def _idea(ctx, *, idea):
    
    idea_responses = [  "Thats a good idea!",
                   "WOW, so creative",
                   "I would try something else",
                   "I dont like that",
                   "I like that"
                    ]
    
    await ctx.send(f'{random.choice(idea_responses)}')
    print('Idea rating machine has spoken')


    #METER
@client.command(aliases=["gayness"])
async def _gayness(ctx):
    
    one_meter = [ "10", "9", "8", "7", "6", "5", "4", "3", "2", "1",
                  "20", "19", "18", "17", "16", "15", "14", "13", "12", "11",
                  "30", "29", "28", "27", "26", "25", "24", "23", "22", "21",
                  "40", "39", "38", "37", "36", "35", "34", "33", "32", "31",
                  "50", "49", "48", "47", "46", "45", "44", "43", "42", "41",
                  "60", "59", "58", "57", "56", "55", "54", "53", "52", "51",
                  "70", "69", "68", "67", "66", "65", "64", "63", "62", "61",
                  "80", "79", "78", "77", "76", "75", "74", "73", "72", "71",
                  "90", "89", "88", "87", "86", "85", "84", "83", "82", "81",
                  "100" "99", "98", "97", "96", "95", "94", "93", "92", "91",
]
    
    await ctx.send(f'You are **{random.choice(one_meter)}%** gay. :rainbow_flag:')
    print('Measured gayness')
    

    




