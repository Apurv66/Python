import json

data = {
    "name": "Dipak",
    "age": 20,
    "skills": ["Python", "Java"]
}

with open("data.json", "w") as f:
    json.dump(data, f)
