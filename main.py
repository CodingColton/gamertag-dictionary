import json

filename = 'data.json'

with open(filename, 'r') as r_obj:
    users = json.load(r_obj)

print("Press 'q' at any time to quit.")

while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    
    gamertag = input("What is your gamertag? ")
    if gamertag == 'q':
        break

    users[name] = gamertag

print(users)

with open(filename, 'w') as f_obj:
    json.dump(users, f_obj)
    print(f_obj)