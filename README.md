# Facebook_public_page_scraper
A dockerized facebook scrapping service using fastAPI, MongoDB and Docker Compose


## This service scrapes Facebook public page posts and saves the data in MongoDB.

The API is built with fastAPI, Facebook scraping is done with facebook scraper python library, and the connection to MongoDB is done with pymongo.

### Steps 

- Run with docker compose :
```
docker-compose up
```
###### or 

- Build an image named "fb_scraper_page"
```
docker build -t fb_scraper_page .
```
- Run the docker image and test it locally with :
```
docker run -d -p 8000:8000 -d fb_scraper_data
```
- You can test http://localhost:8000/docs


- This request would scrap posts from the page "Data Science For u"
 http://localhost:8000/scrap/datascience4u


![image](https://user-images.githubusercontent.com/62955267/182714643-68f03cb0-27d6-4785-a004-fb2f75e554c4.png)

### Running tests 

- To run our tests, we use pytest 
```
pytest
```

