d = {"one" : 
        {"species" : "dog", "colour": "black" },
    "two" :
        {"species" : "cat", "colour" : "ginger"},
    "three" :
        {"species" : "dragon", "colour": "green"}
}

print(d) 
print("\n")

print(d["two"])
d["two"]["colour"] = "tabby"
print(d["two"])

for x in d["three"].values():
    print(x)

d.setdefault("four",True)
print(d)
d.setdefault("four",False)
print(d)