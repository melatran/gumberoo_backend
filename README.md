# Gumberoo Backend
About this...

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

## Getting Started

## Running the Test Suite

## End Points

**Get** `/api/v1/teachers`

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
