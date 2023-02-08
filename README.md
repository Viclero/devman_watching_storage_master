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
 * DB_URL

Run mode setting
 * DEBUG=True - for developer(debug console)
 * DEBUG=False  - for user

.env example:
```
DB_URL="postgres://watch:pass5@checkpoint.domen.org:5434/checkpoint"
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
