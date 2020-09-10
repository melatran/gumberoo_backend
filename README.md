# Gumberoo Backend
Click [here](https://gumberoo-backend.herokuapp.com/) to view Gumberoo's API

Gumberoo is ...

**Contributers**

[Derek Borksi](https://github.com/dborski)

[Max Mitrani](https://github.com/Lithnotep)

[Melanie Tran](https://github.com/melatran)

## Quick Links

* [Software Requirements](#software-requirements)
* [Getting Started](#getting-started)
* [Test Suite](#running-the-test-suite)
* [End Points](#end-points)

## Software Requirements
<img width="764" alt="Screen Shot 2020-09-09 at 7 47 24 PM" src="https://user-images.githubusercontent.com/59414750/92672152-4eaae580-f2d5-11ea-8e8c-decb396f188e.png">

- [Python 3.8.5](https://www.python.org/download/releases/3.0/)
- [Django 3.1.1](https://www.djangoproject.com/)
- [Pip 20.1.1](https://pip.pypa.io/en/stable/)
- [TravisCI](https://travis-ci.org/)
- [PostgreSQL](https://www.postgresql.org/docs/9.3/app-psql.html)

## Getting Started

1. Fork this repository and clone it down
2. Setup a virtualenv

    a. `python3 -m venv myenv`
    
    b. `source myenv/bin/activate`
    
3. Run `pip install -r requirements.txt` to install libraries
4. Create data in PosgreSQL

    a. `$ psql`
    
    b. `$ CREATE DATABASE gumberoo;`
    
    c. `$ \q`
5. Run Migrations

    a. Run `python manage.py makemigrations`
    
    b. Run `python manage.py migrate`

## Running the Test Suite
To check if tests are passing, run `python ./manage.py test`

## End Points

**GET** `/api/v1/teachers`  (Get a list of all teachers)

*Response*
```
[
    {
        "id": 1,
        "first_name": "Sevrus",
        "last_name": "Snape"
    },
    {
        "id": 2,
        "first_name": "Minerva",
        "last_name": "McGonagall"
    },
    {
        "id": 3,
        "first_name": "Albus",
        "last_name": "Dumbledore"
    }
]
```

**POST** `/api/v1/teachers` (Create a new teacher)

*Body*
```
{
    "first_name": "Remus",
    "last_name": "Lupin"
}
```

*Response*
```
{
  "id": 4,
  "first_name": "Remus",
  "last_name": "Lupin"
}
```

**GET** `/api/v1/teachers/:teacher_id` (Get information about a teacher by teacher_id)

*Response*
```
{
    "id": 1,
    "first_name": "Sevrus",
    "last_name": "Snape"
}
```

**POST** `/api/v1/teachers/{teacher_id}/students` (Create students for a teacher)

*Body*
``` data = {
      'id': 1,          
      'students': [   
      {   
        'first_name': 'newStudent1First',  
        'last_name': 'newStudent1Last',  
        'age': 9   
        },   
        {   
        'first_name': 'newStudent2First',   
        'last_name': 'newStudent2Last',   
        'age': 10   
        }   
      ]   
    }.   
```

*Response*   
```
[   
    {   
        "teacher": 1,   
        "id": 7,   
        "first_name": "newStudent1First",   
        "last_name": "newStudent1Last",  
        "age": 9   
    },   
    {   
        "teacher": 1,   
        "id": 8,   
        "first_name": "newStudent2First",   
        "last_name": "newStudent2Last",   
        "age": 10   
    }   
]
```
    
**GET** `/api/v1/teachers/{teacher_id}/students` (Get all students for a teacher)    

*Response* 
```
 [   
    {   
        "teacher": 1,   
        "id": 1,   
        "first_name": "newStudent1First",   
        "last_name": "newStudent1Last",   
        "age": 9   
    },   
    {   
        "teacher": 1,   
        "id": 2,   
        "first_name": "newStudent2First",   
        "last_name": "newStudent2Last",   
        "age": 10   
    }   
  ]     
 ```
 **POST** `/api/v1/students/:student_id` (Create a lesson for a student when they take the checkpoint for a lesson)
 
 *Body*
 ```
 {
    "lesson": 2,
    "score": 1,
    "mood": "I don't understand anything"
 }
 ```
 
 *Response*
 ```
 {
    "student": 3,
    "lesson": 2,
    "score": 1,
    "mood": "I don't understand anything"
 }
 ```
