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
 * DB_ENGINE
 * DB_HOST
 * DB_PORT
 * DB_NAME
 * DB_USER
 * DB_PASSWORD

Run mode setting
 * DEBUG=True - for developer(debug console)
 * DEBUG=False  - for user

.env example:
```
DB_ENGINE='django.db.backends.postgresql_psycopg2' 
DB_HOST='checkpoint.domen.org'
DB_PORT='5434'
DB_NAME='checkpoint'
DB_USER='watch'
DB_PASSWORD='pass5'
DEBUG=False 
SECRET_KEY ="8ldb6*n=vwy*$" 
```

SECRET_KEY generate
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
## to Start
Run serven on Localhost
```
python manage.py runserver 0.0.0.0:8000
```

UI is available in browser 
* http://127.0.0.1:8000/
