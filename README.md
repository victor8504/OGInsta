# OGInsta

#### This is a photo posting website created using Django., 17/06/2018


#### By **[Victor NJuguna](https://github.com/victor8504)**

## Description
[This](https://oginsta.herokuapp.com/) is a photo posting website created using Django. A user with an account can:
* post images with captions
* view list of other users
* comment on a post

## User Stories
As a user I would like:
* to sign in to use the application
* to upload photos
* to see my profile with my posts
* to follow others and see their picture on my timeline
* to like a picture and leave a comment on it
* download a picture and save it to my machine

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display sign up for | N/A | Display sign up form when a user visits the site |
| Create an account | Fill the sign up form and **click submit** | Create an account and profile for the user and log the user into the site |
| Display current user's profile | **Click** the user name | Display the current user's profile page with their posts |
| Upload a post | **Click**  post | Direct the user to a page with a form where the user can create and submit a post |
| See other users | **Click** friends | Direct the user to a page where they see a list of other users |
| Comment on post | **Click** comment link | Direct user to a page with a form for writing a comment |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database


### Installation Process
```
git clone https://github.com/victor8504/oginsta.git && cd cd the-gram
virtualenv virtual or python3.6 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
```
* Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
USER=<your postgresql username>
PASSWORD=<your postgresql password>
```
* Create Postgres Database
```
psql
CREATE DATABASE instagram;
```
### Running the application
```
./manage.py runserver or python3.6 manage.py runserver
```

### Running the tests
```
./manage.py test or python3.6 manage.py test
```

## Known Bugs

A number of user story functionalities are not yet enabled


## Technologies Used
- Python3.6
- Django
- Bootstrap
- Postgres Database
- CSS
- HTML
- Heroku

### License

MIT (c) 2017 **[Victor Njuguna](https://github.com/victor8504)**


