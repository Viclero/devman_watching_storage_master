# Description

UI for storage users control


## Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
``` 

## Environment variables
Location is  .env

for DB connection
 * HOST
 * USER
 * PASSWORD

Run mode setting
 * DEBUG=True - for developer(errorsview)
 * DEBUG=False  - for user

.env example:
```
HOST='checkpoint.domen.org'
USER='watch'
PASSWORD='pass5'
DEBUG=False
```

## to Start
Run serven on Localhost
```
python manage.py runserver 0.0.0.0:8000
```

UI is available in browser 
* http://127.0.0.1:8000/
