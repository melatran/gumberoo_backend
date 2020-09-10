# Gumberoo Backend
Click [here](https://gumberoo-backend.herokuapp.com/) to view Gumberoo's API

Gumberoo is ...

**Contributers**

[Derek Borski](https://github.com/dborski)

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
 ### Teacher Lesson Endpoints
 
 **GET** `/api/v1/lessons/:lesson_id`  (Get a specific lesson)  

 *Response*

```python
{
  'id': 1,
  'name': 'Lesson 1',
  'questions': [
    {
      'id': 1,
      'question': 'Question 1',
      'reading': 'Reading 1',
      'answers': [
        {
          'id': 1,
          'answer': 'Answer 1 Text',
          'correct': False
        },
        {
          'id': 2,
          'answer': 'Answer 2 Text',
          'correct': True
        }
      ]
    },
    {
      'id': 2,
      'question': 'Question 2',
      'reading': 'Reading 2',
      'answers': [
        {
          'id': 3,
          'answer': 'Answer 3 Text',
          'correct': True
        },
        {
          'id': 4,
          'answer': 'Answer 4 Text',
          'correct': False
        }
      ]
    }
  ],
  'teacher': {
    'id': 1,
    'first_name': 'teacher1First',
    'last_name': 'teacher1Last'
  }
}
```

**POST** `/api/v1/teachers/:teacher_id/lessons`  (Create a new lesson for a specific teacher)  

 *Request*
 ```python
 {
  'lesson': {
    'name': 'lessonName1',
    'questions': [
        {
          'question': 'question1 description',
          'reading': 'question1 reading',
          'answers': [
              {
                'answer': 'answer1 description',
                'correct': False
              },
              {
                'answer': 'answer2 description',
                'correct': False
              },
              {
                'answer': 'answer3 description',
                'correct': True
              },
              {
                'answer': 'answer4 description',
                'correct': False
              }
            ]
        },
        {
          'question': 'question2 description',
          'reading': 'question2 reading',
          'answers': [
              {
                'answer': 'answer1 description',
                'correct': False
              },
              {
                'answer': 'answer2 description',
                'correct': False
              },
              {
                'answer': 'answer3 description',
                'correct': True
              },
              {
                'answer': 'answer4 description',
                'correct': False
              }
            ]
          }   
      ]
  }
 }
 ```

 *Response*
 
```python
{
  'id': 1,
  'name': 'lessonName1',
  'questions': [
    {
      'id': 1,
      'question': 'question1 description',
      'reading': 'question1 reading',
      'answers': [
        {
          'id': 1,
          'answer': 'answer1 description',
          'correct': False
        },
        {
          'id': 2,
          'answer': 'answer2 description',
          'correct': True
        },
        {
          'id': 3,
          'answer': 'answer3 description',
          'correct': False
        },
        {
          'id': 4,
          'answer': 'answer4 description',
          'correct': False
        }
      ]
    },
    {
      'id': 2,
      'question': 'question2 description',
      'reading': 'question2 reading',
      'answers': [
        {
          'id': 3,
          'answer': 'answer1 description',
          'correct': True
        },
        {
          'id': 4,
          'answer': 'answer2 description',
          'correct': False
        },
        {
          'id': 5,
          'answer': 'answer3 description',
          'correct': True
        },
        {
          'id': 6,
          'answer': 'answer4 description',
          'correct': False
        }
      ]
    }
  ],
  'teacher': {
    'id': 1,
    'first_name': 'teacher1First',
    'last_name': 'teacher1Last'
  }
}
```
