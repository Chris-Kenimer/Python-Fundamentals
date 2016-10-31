users = {
    'Students': [
        {'first_name' :  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
    }
for key, data in users.items():
     print key
     for index, value in enumerate(data):
        nameLen = len(value["first_name"])
        nameLen += len(value["last_name"])
        print str(index + 1 ),"-",value["first_name"].upper(),value["last_name"].upper(),"-", nameLen
