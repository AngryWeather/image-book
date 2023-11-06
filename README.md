# ImageBook
ImageBook is a project that allows users to share images. It's similar in function to https://imgur.com/.

## Installation
```
# clone this repository
https://github.com/AngryWeather/image-book.git

# install dependencies
pip install -r requirements.txt

# create 2 files needed to run in development mode
- db.sqlite3
- .env in subdirectory image_book where settings.py file exists

.env needs to have SECRET_KEY field

# start local server
python manage.py runserver
# go to localhost:8000
```
