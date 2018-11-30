#This is code for a rule based bot 
import time
import random
import requests

name = input("Hello, what is your name? ")

time.sleep(2)
print("Hello " + name)

feeling = input("How are you today? ")

#feelings_happy = ("happy","cheerful","hopeful","good","great","awesome")
#feelings_sad = ["sad"," annoyed"," angry"," ashamed"]

time.sleep(2)
if "good" or "Good" in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")

time.sleep(2)
def fav_colour(colour):
    fav_colour = input("What's your favourite colour? ")
    colour = ["Red","Green","Blue"]

time.sleep(2)
print("You got some taste. Yes absolutely My favourite colour is " + random.choice(colour))

time.sleep(2)
holidays = input("I can't wait till christmas. Are you excited? ")
if "Yes" in holidays:
    print("I knew you would get in the holiday spirit")
else:
    print("Don't be such a grinch")
    
time.sleep(2)
presents = input("What do you want for christmas? ")

time.sleep(2)
print("Ooooo Fancy. " + "I want to get a new hockey stick ")

time.sleep(2)
favsport = input("Speaking of sports, What's your favourite sport? ")

sport = ["Basketball","Tennis","Football","Rugby","Soccer","Badminton","Boxing","Archery"]

time.sleep(2)
if favsport in sport:
    print("My favourite sport is " + random.choice(sport))
else:
    print("I would suggest trying " + random.choice(sport))
    
time.sleep(2)
print("Since you love sports so much let me check the weather for you!")

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=d96d08b24ca0aa3503fe9454eb2b93ef&q='
city = input("City name: ")

url = api_address + city

json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['main']
print(formatted_data)

time.sleep(2)
print("I think you are good for today to play " + favsport)

time.sleep(2)
coursework = input("How are you finding BSc Computer Science so far? ")

opinions = ["I'm enjoying it","I love it","It could be better","I hate it","It's alright","It's good", "It's decent"]

time.sleep(2)
if ["good","love","enjoying"] in opinions:
    print("I'm glad you enjoy it. In my opinion " + random.choice(opinions))
else:
    print("Ahh well I enjoy it. Let's study sometime")
    
time.sleep(2)
fav_food = input("What's your favourite type of food? ")

foodtypes = ["Chinese", "Mexican", "Indian", "Caribbean", "Italian", "Japanese", "Spanish"]

time.sleep(2)
if fav_food in foodtypes:
    print("Yummmmm! I like your style")
else:
    print("Hmmm, I've never tried it. We should go out to eat sometime")
