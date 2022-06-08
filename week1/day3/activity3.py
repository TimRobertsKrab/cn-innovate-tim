fav_songs = [
            {"artist": "Kate Bush","song_name":"Running up that hill",
            "genre":"New wave","release_year":"1985"}]


fav_songs.append({"artist":"A-ha","song_name":"The sun always shines on T.V",
            "genre":"Pop","release_year":"1985"})

for d in fav_songs:
    print(d.values())

print("Add extra entry to dictionaries")
for d in fav_songs:
    d["extra"] = "blank"

for d in fav_songs:
    print(d.values())

print("Remove the first entry of the first dictionary")
fav_songs[0].pop("artist")
print(fav_songs[0])

print("Change genre of the second entry")
fav_songs[1]["genre"] = "Alternative/Indie"
print(fav_songs[1])
