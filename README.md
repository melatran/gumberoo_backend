# gumberoo_backend

**POST** api/v1/teachers/{teacher_id}/students example request.  
Body:       
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
    .    
expected response.    
    `[   
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
]  `   
    
Get all Students for a teacher: **GET** api/v1/teachers/{teacher_id}/students.    
expected response.   
` [   
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
  `   