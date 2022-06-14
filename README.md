
### Project_Runaway

## Project Description

### A website application designed to allow user post projects , receive rating from other various users based on each project design, usability and content.
### Inside the websites users can creat their own accounts and Profile details.

## Getting Started

- Create a repository on Github.
- Create a new directory in the terminal and initialize it
- Open your choice editor and start creating your code.
- When you are done with the project,deploy it to Heroku.
- Host your Heroku link as your live link on your created Github repository.

## Screenshot
https://raw.githubusercontent.com/2BWeru/Project-Review/master/static/images/Screenshot_2022-06-14_03-01-36.png

https://raw.githubusercontent.com/2BWeru/Project-Review/master/static/images/Screenshot_2022-06-14_09-57-50.png


## Prerequisites

- Python3
- Django
- virtual environment
- rest_framework
- Postman

### User story
- User can create an account
- User can log in /Log out of their accounts
- User can upload projects,Ip
- Other users can view projects available in the website.
- Users can rate projects by design, usability and  content
- User can see average rating of a project.
- User can give reviews on different projects.
- User can see other peoples reviews on various projects
- User can view their profile ,
- User can create their profile 
- Search projects present
- See project description and landing page  when they click the project 
- Use API to get data input in  Profile and Projects model.


## Deployment
### Heroku url  - https://project-runaway4.herokuapp.com/


## Deployment
- log in to heroku
```
heroku login
```
- create heroku app
```
heroku create app
```
- Upload requirements
```
pip freeze
```
- create a postgres addon to your heroku app
```
heroku addons:create heroku-postgresql:hobby-dev
```
- push to heroku

```
git push heroku master
```
- run migrations
```
heroku run python manage.py migrate
```
## Contact Information
- For any inqueries feel free to write to me through :
  - (betty.weru@student.moringaschool.com)

## Licence
- MIT License
- Copyright (c) 2022 Betty Weru
