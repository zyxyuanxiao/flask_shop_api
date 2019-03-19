# Flask Shop API

REST API which exposes endpoints both for an online shop and a CMS admin. It's developed using flask framework which runs as a socketio server.

## Setup

**Requirements**

* Virtualenv
* Redis
* Heroku CLI


**Setup**

    $ virtualenv <envname> -p python3
    $ source <envname>/bin/activate
    $ pip install -r requirements.txt

**Add dotenv to project root**

You should create a .env file on the project root. You can get this on the repo url https://github.com/hivisasapro/hivisasa-stage-dotenv

**Running app using heroku cli**

    $ heroku local web
    
**Running app using manage.py**

    $ python manage.py run server

**Running app using gunicorn**

    $ gunicorn --worker-class eventlet -w 1 wsgi:app

