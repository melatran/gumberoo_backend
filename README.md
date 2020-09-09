# gumberoo_backend

## Teacher Students. 
Create Student: POST api/v1/teachers/{teacher_id}/students
example Body:   
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
Get all
