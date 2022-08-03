# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 23:51:39 2022

@author: anwar
"""

# import necessary libraries
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from facebook_scraper import get_posts
from pymongo import MongoClient
#import uvicorn




#  create a FastAPI instance
app = FastAPI()

# get the MongoDB database connection

#Create a new MongoClient
client = MongoClient("localhost", 27017)  
db = client["facebook_scraper"] # mongodb Database
collection = db["posts"] # collection inside facebook_scraper database



#function to insert one post in mongo database
def save_post(post):
    return collection.insert_one(post)

#function to insert multiple posts in mongo database
def save_posts(posts):
    return collection.insert_many(posts)

#function to find posts
def find_posts(page_name = None):
    if page_name is None : 
        return list(collection.find())
    return list(collection.find({'username' : page_name}))



@app.get("/",include_in_schema=False)
async def redirect():
    return RedirectResponse(url='/docs')


@app.get("/scrap/{page_name}",summary="Scraps posts from page facebook by name")
async def scrap_posts(page_name):
    posts = []
    try:
        posts = list(get_posts(page_name, pages=1))
        posts = [delete_none(post) for post in posts]
        save_posts(posts)
    except:
        pass
    return posts


@app.get("/scrap/{page_name}/{nbr_pages}",summary="Scraps posts from facebook by page name and number of pages")
async def scrap_pages(page_name, nbr_pages):
    posts = []
    try:
        print("here")
        posts = list(get_posts(page_name, pages=int(nbr_pages)))
        posts = [delete_none(post) for post in posts]
        save_posts(posts)
    except Exception as e:
        print(e)
    return posts

@app.get("/read_all",summary="find all stored posts in database")
async def find_all():
    response = dict()
    posts = find_posts()
    response["total"] = len(posts)
    response["posts"] = posts
    return response


@app.get("/read/{page_name}",summary="find stored posts by page name in database")
async def find_by_name(page_name):
    response = dict()
    posts = find_posts(page_name)
    response["total"] = len(posts)
    response["posts"] = posts
    return response


def delete_none(d):
    new_dict = dict()
    for k, v in d.items():
        if v:
            new_dict[k] = v
    new_dict["_id"] = new_dict["post_id"]
    return new_dict



# if __name__ =='__main__':
#      uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")      