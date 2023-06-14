# June 10, 2023
# Homework 2, Part 2

# PART TWO: Lists

nations = ["France", "Canada", "Ethiopia", "Poland", "Algeria", "Japan", "Mexico"]
for nation in nations:
    print("One country is", nation)
nations.sort()
print("The first country in the list after it is sorted is",nations[0])
print("The second-to-last country in the list after it is sorted is",nations[-2])
nations.remove("France")

for nation in nations:
    print("One country in all caps is", nation.upper())

# PART TWO: Dictionaries

tree = {
    'name': 'Abies amabilis',
    'species': 'evergreen conifer',
    'age': '400',
    'location_name': 'Seattle, Washington, USA',
    'latitude': 47.608013,
    'longitude': -122.335167
}

print(tree['name'], "is a", tree['age'], "year-old tree that is in", tree['location_name'])

if 40.7128 - 47.608013 > 0:
    print ("The", tree['name'], "in", tree['location'], "is south of NYC") 
else:
    print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC")

user_age=input("How old are you? ")
user_age=int(user_age)
tree['age']=int(tree['age'])
difference=abs(user_age - tree['age'])

if user_age - tree['age'] > 0:
    print("You are", difference, "years older than the", tree['name'], "tree")
else:
    print(tree['name'], "was", difference, "years old when you were born")

# PART TWO: Lists of dictionaries

places = [
    {'city': 'Moscow', 'latitude': 55.75, 'longitude': 37.62 },
    {'city': 'Tehran', 'latitude': 35.55, 'longitude': 51.13 },
    {'city': 'Falkland Islands', 'latitude': -51.56, 'longitude': -59.82 },
    {'city': 'Seoul', 'latitude': 37.53, 'longitude': 127.02 },
    {'city': 'Santiago', 'latitude': -33.45, 'longitude': -70.67 }
]

for place in places:
    if place['latitude'] > 0:
        print(place['city'], "is above the equator.")
    if place['latitude'] < 0:
        print(place['city'], "is below the equator.")
    if place['city'] == 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

for place in places:
    if place['latitude'] > tree['latitude']:
        print(place['city'], "is north of the", tree['name'])
    if place['latitude'] < tree['latitude']:
        print(place['city'], "is south of the", tree['name'])