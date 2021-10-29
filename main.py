from fastapi import FastAPI, Request
from facebook_scraper import get_posts
import datetime

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()
client = MongoClient("localhost", 27017)
db = client['posts']

@app.get("/")
async def root():
    return "Welcome to facebook scrapper"

@app.get("/scrap/")
async def scrap_posts(page: str, limit: int = 2, save: bool=False):
    res = {}
    res["result"] = [post for post in get_posts(page, pages=limit)]
    res["time"] = datetime.datetime.now()
    
    if save:
        try: 
            db.posts.insert_many(res["result"])
            return "saved successfully"
        except:
            return "saving error"
    return res["result"]

@app.get("/post/")
async def get_post(post_id: str):
    document = db.posts.find_one({'post_id': post_id}, {'_id': 0})
    print(document)
    return document


@app.get("/load/")
async def load_data(request: Request):
    params = {item[0]: item[1] for item in request.query_params.multi_items() }
    res = db.posts.find(params, {'_id': 0})
    return [i for i in res]
