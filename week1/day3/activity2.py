countries = {"United Kingdom":"London", "France":"Paris",
            "Germany":"Berlin","Spain":"Madrid","Italy":"Rome"}

countries.setdefault("Belgium","Brussels")
countries.setdefault("Portugal","Lisbon")

print("List of tuples\n")
for i in countries.items():
    print(i)

print("List of countries(keys)")
for country in countries.keys():
    print(country)

print("List of capital cities(values)\n")
for capital_city in countries.values():
    print(capital_city)

languages = ["English","French","German","Spanish","Italian","French","Portuguese"]

print("Change the capital cities to national language")
# countries["United Kingdom"] = "English"
# countries["France"] = "French"
# countries["Germany"] = "German"
# countries["Spain"] = "Spanish"
# countries["Italy"] = "Italian"
# countries["Belgium"] = "French"
# countries["Portugal"] = "Portuguese"

# i=0
# for c in countries:
#     countries[c] = languages[i]
#     i+=1

for a,b in zip(countries.keys(),languages):
    countries[a] = b

for i in countries.items():
    print(i)
