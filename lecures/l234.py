ourdicr = { 
    "make" : "Ford",
    "Model" : "Mustang",
    "Year" : "1966",
    "Color" : "Red",
}

print(ourdicr)
print(ourdicr["make"])


ourdicr["Color"] = "Blue"
for key in ourdicr:
    print(ourdicr[key])

for values in ourdicr.values():
    print(values)

for key, values in ourdicr.items():
    print(key,":", values)