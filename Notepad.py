#This was inspired by a youtube tutorial, link:https://www.youtube.com/watch?v=pEnRUKhAcOM
import discord
import asyncio
import random
import pickle
#The pickle module changes a data from it's complex state into a form which is easier to access
import os
#The os module allows us to interface with the underlying operating system, hence the linux os

client = discord.Client()

@client.event
async def on_ready():
    print("logged in as Armani Williams")
    print("Stephen's BOT")
    print("Client ID")
    print("I'm finally alive")
    
@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await client.send_message(message.channel, 'Hello, How are you doing?')

        def check(msg):
            return msg.content.startswith("good")

        message = await client.wait_for_message(author=message.author, check=check)
        mood = message.content[len('$hello'):].strip()
        await client.send_message(message.channel, "That's great to hear!".format(mood)) 
            
@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        await client.send_message(message.channel, "Hello, hope you are doing well?.")
#This heads and tails area was inspired by the Rapptz Github, link:https://github.com/Rapptz/discord.py/blob/async/examples/guessing_game.py        
    elif message.content.startswith("!flip"):
        flip = random.choice(["Heads" , "Tails"])
        await client.send_message(message.channel, flip)
    elif message.content.startswith("!addquote"):
        if not os.path.isfile("quote_fle.pk1"):
            quote_list = []
#This allows the user to add a quote in real time using the command !addquote. They can then see the quote whenever they need to using the command !quote        
        else:
            with open("quote_file.pk1", "rb") as quote_file:
                quote_list = pickle.load(quote_file)
        quote_list.append(message.content[9:])        
        with open("quote_file.pk1", "wb") as quote_file:
            pickle.dump(quote_list, quote_file)
    elif message.content.startswith("!quote"):
        with open("quote_file.pk1", "rb") as quote_file:
            quote_list = pickle.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))
#The piece of code which deals with files was helped by the youtube tutorial,link:https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=1078s        

client.run("TOKEN")
          
