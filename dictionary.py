
dictionary = {
    "name": "Dhruvi",
    "age" : 20,
    "sub" : ["phy", "chem", "math"]
}

print(dictionary["name"])
print(dictionary.keys())
print(dictionary.values())
print(list(dictionary.items()))
print(dictionary.get("name"))

dictionary.update({"gender" : "Female"})

print(dictionary)
