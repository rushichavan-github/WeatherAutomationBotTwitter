import tweepy
import time
import requests
import json
from PIL import Image, ImageFont, ImageDraw
import datetime

consumer_key = 'zrgz8HNXV5Ltyd2hhtQaz0cZn'
consumer_secret = 'oXZ6lXqjf0MgTuc7dgggVOOWANNFZwnSd9cbh9qJfrsKyEaVDe'
key = '1304621202237919234-xMphi4yTRdhKSeYcgVwBJn7r2aoC9g'
secret = 'opO5wloSnjk6RWozvYhzFWqNqrbHsIrTr2wepCY4Fpsi0'

api_key = "6050800a00ca0213a9f1fab9b58013a1" #Update Your API Here
position = [300, 430, 555, 690, 825]

india_list = ["Bidar", "Delhi", "Mumbai", "Kolkata", "Jaipur"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

def weather():
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=50)
    content = "Latest Weather Forecast (SRC-PAA)"
    color = 'rgb(255, 255, 255)'
    (x, y) = (55,50)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=30)
    x = datetime.datetime.now()
    content = x.strftime("%A - %B %d, %Y, %X")
    color = 'rgb(255, 255, 255)'
    (x, y) = (55,145)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in india_list:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype('Inter.ttf', size=50)
        color = 'rgb(0, 0, 0)'
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255, 255, 255)'
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255, 255, 255)'
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1

    image.save("new.png")

    tweet_text = "Weather Report After Every 4hours (Automation)"
    image_path = "new.png"
    #Generate text tweet with media (image)
    status = api.update_with_media(image_path, tweet_text)

while True:
    weather()
    time.sleep(14400)
