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
## Technologies
- Django
- Bootstrap5
- Tests: Django's unittest

## To Do
- Profile page
- Edit and delete posted images
- Edit and delete comments
- Reply to comments
- Search for specific post
- Follow favorite users
- Notifications

## Features
### Register
![image](https://github.com/AngryWeather/image-book/assets/105065960/0c11a046-6e55-40ce-baf9-f7631b724630)
### Login
![image](https://github.com/AngryWeather/image-book/assets/105065960/3835e918-e52d-4c6a-a1d4-7577cebb0262)
Logged in users can add images and post comments.

### Adding Images
![image](https://github.com/AngryWeather/image-book/assets/105065960/4b03515a-8528-4fb8-aa8c-3f66dd55026f)
After adding an image the user is taken to the detail page:

![image](https://github.com/AngryWeather/image-book/assets/105065960/177f63b4-6920-4aa5-85fa-d9b18260d825)

### Comments
Logged in users can also add comments:

![image](https://github.com/AngryWeather/image-book/assets/105065960/0955e925-62ec-487b-a556-985e31146117)
![image](https://github.com/AngryWeather/image-book/assets/105065960/6a5884a5-9b18-4d42-b4d1-f8ad7fbca20e)

### Homepage
The homepage consists of all uploaded images displayed responsively with the newest image presented first.

![image](https://github.com/AngryWeather/image-book/assets/105065960/3b8a1276-9039-44c5-811b-a6676060cf3c)
![image](https://github.com/AngryWeather/image-book/assets/105065960/25c2bf48-46c1-4b0b-ad32-95c3e8eee4e2)

