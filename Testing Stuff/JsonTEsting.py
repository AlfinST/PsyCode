import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y =[ ("tag","value"),("tag","value"),("tag","value")]
 


# print(json.dumps(x,indent=4))

print("\n\n",json.dumps(y,indent=4,\
     separators=(", ", " : ")))
