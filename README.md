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

**GET** `/api/v1/teachers`

## Teacher Students. 
4
Create Student: POST api/v1/teachers/{teacher_id}/students
5
example request Body:   
6
` data = {
7
      'id': 1,
8
      'students': [
9
        {
10
        'first_name': 'newStudent1First',
11
        'last_name': 'newStudent1Last',
12
        'age': 9
13
        },
14
        {
15
        'first_name': 'newStudent2First',
16
        'last_name': 'newStudent2Last',
17
        'age': 10
18
        }
19
      ]
20
    }.
21
    `. 
22
    expected response. 
23
  `[
24
    {
25
        "teacher": 1,
26
        "id": 7,
27
        "first_name": "newStudent1First",
28
        "last_name": "newStudent1Last",
29
        "age": 9
30
    },
31
    {
32
        "teacher": 1,
33
        "id": 8,
34
        "first_name": "newStudent2First",
35
        "last_name": "newStudent2Last",
36
        "age": 10
37
    }
38
]  `
39
    
40
Get all Students for a teacher: GET api/v1/teachers/{teacher_id}/students. 
41
expected response. 
42
` [
43
    {
44
        "teacher": 1,
45
        "id": 1,
