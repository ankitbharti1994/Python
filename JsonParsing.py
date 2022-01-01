import json
import os
import django

# convert string to json
person = '{"name": "ankit", "visited_place": ["Hyderabad", "Mumbai", "Bangalore", "Delhi", "Daman"]}'
print(person)

person_json = json.loads(person)
print(person_json['visited_place'])

# read json from file and convert to dictionary
with open('person.json') as f:
    person1 = json.load(f)

print(person1)
print(person1[0]['name'])

# convert dictionary to json object
json_object = json.dumps(person)
print(json_object)

with open('user.json', 'w') as f:
    json.dump(person, f)

print(django.get_version())