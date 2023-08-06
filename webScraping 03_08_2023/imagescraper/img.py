#import the libraries
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import pymongo
# create a logging file
logging.basicConfig(filename="img_scrapper.log", level=logging.INFO)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template('index.html')


@app.route("/search", methods=["POST"])
def index():
    if request.method == "POST":
        try:
            query = (request.form['content'].replace(" ", ""))

            # create a directiory to store the images
            save_dir = "images/"

            # check directory exists or not
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # create a fake agent to avoid getting blocked to the Google

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

            # seacrh the images
            response = requests.get(
                f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")

            # Apply the Beautiful soup to the response
            Beautiful_soup = BeautifulSoup(response.text, "html.parser")

            # find the img tag in response
            img_tags = Beautiful_soup("img")

            # delete the first element of the list
            del img_tags[0]
            # Create a empty list to store the images
            img_data = []

            # loop through the img tags
            for index, img_tag in enumerate(img_tags):
                # get featch the url of the image
                img_url = img_tag["src"]
                print(img_url)

                # Trigger the url to featching the images
                image_data = requests.get(img_url).content

                # Create a dictionary
                dict = {"Index": index, "Image": image_data}

                # append the dictionary to the list
                img_data.append(dict)

                # save the images in the folder

                with open(os.path.join(save_dir, f"{query}_{img_tags.index(img_tag)}.jpg"), "wb") as f:
                    f.write(image_data)

            # store the data in the database
            client = pymongo.MongoClient(
                "mongodb+srv://prashantjadhav9089:prashant9089@bdi.lp6fpze.mongodb.net/?retryWrites=true&w=majority")
            db = client['img_scrapper']
            collection = db['imges_data']
            collection.insert_many(img_data)

            return "images are Loaded....!!"

        except Exception as e:
            logging.error(e)
            return "Something went wrong"
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9089, debug=True)
