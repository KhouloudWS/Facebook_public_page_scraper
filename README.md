# Facebook_public_page_scraper
A dockerized facebook scrapping service using fastAPI



* This project is an API meant to scrape posts from Facebook public pages using either page id or page name then store the posts into a mongo-db database. Posts have a unique ID named post_id in the database and can be a good way to identify posts in the database. 
* The API is built using fastAPI, the Facebook scraping functionality is thanks to facebook_scraper python library, and the connection to mango-db is made by pymongo. 
* This repository contains a requirement.txt file that contains the required python libraries needed for this project, a main.py containing the project's code, and a Dockerfile that can be used to build a docker for the API.
## Usage

To build a docker named “fb_scraper” for the API please run this command in the same directory as main.py, Dockerfile, and requirements.txt:


```bash
docker built -t fb_scraper
```
You can later run the docker and test it locally using:
```bash
docker run -p 8000:8000 fb_scraper
```
To start a docker server instance for the database please run:
```bash
docker run --name fbdb -d mongo
```
This will create a docker with a mongo-db database, you can fill the dataset with scraped data using the API. 

## Guide
This is a quick guide for using the API routes that are made in the script:

/scrap/ : This route is used for scraping data from Facebook and storing it in the database, please give it the following arguments:
* page : page_id or page_name
* limit (optional, default=2): limit the number of pages of posts to scrape from that page (preferably limit >1 because a lower value might give no results depending on the page)
* save (optional, default=False): if True, the scraped posts would be saved in the database, otherwise they would be just shown on the screen.

/post/ : This is used to retrieve a post from the database using its post_id. Only needed argument is post_id

/load/: This is used to retrieve 1 or multiple posts from the database, you can use any of the possible keys of the schema as arguments.


## Test API
To test the API you can make a localhost either by running the docker, or you can make the API work directly on your computer by installing all the requirements then running the:
```bash
uvicorn main:app --reload
```
Please find below some tests you can try after making the API work:

http://localhost:8000/scrap/?page=theartidote 

The above request would scrap posts from the page “The Artidote”

http://localhost:8000/scrap/?page=theartidote&save=True

The above request would scrap and save the posts in the database

http://localhost:8000/post/?post_id=2657553427872738

The above request would find the post with the id 2657553427872738 in the database

http://localhost:8000/load/?page_id=742359879214163

This request would give you all posts of the page having page_id=742359879214163



