# moviemaster-web
Just another challenge - ITCrowd

# Challenge
A company that has a website about movies wants to provide its customers and users an API to query their database, as well as provide the trusted company users the ability to update or create new records.
In order to complete this, you must create a RESTful interface that will provide access to the company’s database.

# Definition of done
1. Provide a REST API to access movies and persons models.
2. Safe methods are publicly available, no authentication is required.
3. Unsafe methods are only available to authenticated users.
4. Movie documents must include references or full documents to persons in their different
roles.
5. Person documents must include references or full documents to movies in the different
roles the Person has.
6. Movie documents must include the Release Year in roman numerals. This field should
not be stored in the DB, just calculated on the fly.

# List of available endpoints
- /persons/
- /aliases/
- /movies/

# Used libraries/frameworks
- Django 3.0.8
- django-redis-cache
- psycopg2
- djangorestframework
- gunicorn

# Extra credit
1. Project is deployed and running online (AWS, Heroku, cloud servers, own servers…)  
https://moviemaster-web.herokuapp.com
2. User interface to browse items.  
Browse https://moviemaster-web.herokuapp.com/admin -> admin:12345  
3. User interface to create/edit/delete items.  
Browse https://moviemaster-web.herokuapp.com/admin -> admin:12345  
4. Justification of chosen libraries/frameworks against other popular choices.  
I love python.  
I've chosen django as it is one of my favorites frameworks and it's simple to create models and migrations, as well as a rest API. It has lots of libraries to expand funcionality.  
Docker and Docker Compose provide simple, maintainable and scalabble containers to keep up all the stack. The application can be easily deployed over Heroku.  
Redis is used to keep down the server latency and reduce server loads, it works well along with django.  
I've decided not to improve a frontend with a nice UI as my role will probably be a backender, and Django Admin already offers the app data handling, no need to reinvent the wheel.  
I've chosen gunicorn as it is a simple webserver that fits the small requirements for this application and it supports WSGI, offering scalability on demand.

# Prerequisites:
Docker Compose

# Setup
- Clone moviemaster-web
- cd moviemaster-web
- cp .env.dist .env (Any environment specific configuration should be here)
- docker-compose up -d (Should auto-build and get the web server up)

# Run locally
- Open your browser and go to http://localhost:8000

Solved in 8hs 42m.
