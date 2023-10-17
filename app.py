import os
import openai
import requests
from config import key

openai.api_key = key

#openai.api_key = OPENAI_API_KEY

response = openai.Image.create(prompt="a white siamese cat",
                               n=1,
                               size="1024x1024")
image_url = response['data'][0]['url']
print(image_url)

#image_data = requests.get(image_url).content

#with open("siamese_cat.jpg", "wb") as f:
# f.write(image_data)
#print("Image saved successfully.")
#except Exception as e:
# print("An error occurred:", str(e))
#python3 app.py
