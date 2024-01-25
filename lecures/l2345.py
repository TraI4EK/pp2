ourdict = {
    "Car1":{
    "Make" : "Ford",
    "Model" : "Mustang",
    "Year" : "1966",
    "Color" : "Red",
    },
    "Car2":{
    "Make" : "Toyota",
    "Model" : "Camry",
    "Year" : "2018",
    "Color" : "White",
    },
    "Car3":{
    "Make" : "Porshe",
    "Model" : "911 Carrera Turbo s",
    "Year" : "2023",
    "Color" : "Green",
    }
}

print (ourdict)
print(ourdict["Car3"])
print(ourdict["Car3"]["Model"])

ourdict.pop("Car2")

print(ourdict)

ourdict.update({
    "Car2":{
    "Make" : "Porshe",
    "Model" : "911 Carrera Turbo s",
    "Year" : "2023",
    "Color" : "Green",
    }
})

ourdict.pop("Car3")
print(ourdict)