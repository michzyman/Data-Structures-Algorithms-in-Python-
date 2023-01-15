user = {
    "age": 54, 
    "name": 'Kylie',
    "magic": True,
}

print(user["age"])

user2 = dict(
    age = 54, 
    name = 'Jey', 
    magic= True
)

print(user2)

name = user.get("name")


#terate over the key-value pairs in a dictionary
for k , v in user2.items():
    print(k,v)