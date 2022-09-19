import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_labels(url_to_image):
    url = "https://image-labeling1.p.rapidapi.com/img/label"

    payload = {"url": url_to_image}
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.getenv("xrapidAPI_KEY"),
    "X-RapidAPI-Host": "image-labeling1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.json())

if __name__ == "__main__":
    get_labels(sys.argv[1])
