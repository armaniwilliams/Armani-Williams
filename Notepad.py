#This was inspired by a youtube tutorial 
import discord
import asyncio
import random
import pickle
#The pickle module a data from it's complex state into a form which is easier to access
import os
#The os module allows us to interface with the underlying operating system, hence the linux os

client = discord.Client()

@client.event
async def on_ready():
    print("logged in as Armani Williams")
    print("Stephen Filani's life")
    print("506166949428985856")
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
        

client.run("NTA2MTY2OTQ5NDI4OTg1ODU2.Dt7XIg.-6OulBnpCSRzu0CfnfODMX--sqQ")
          
