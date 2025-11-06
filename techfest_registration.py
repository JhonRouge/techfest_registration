print("Welcome to SMIT TechFest!")
print("Event organized by Jhon Rouge Andales of APPDAET BTCS2")
#T1
n_par = int(input("How many participants will register?: "))

if n_par <= 0:
    print("Invalid number of participants.")
    quit()

#T2
par = []
for i in range(n_par):
    name = input("Enter participant name: ")
    track = input("Enter a track: ")
    par.append({"name": name,"track": track})

print("registered participants: ")
for i, p in enumerate(par,1):
    print(f"{i}. {p['name']} - {p['track']}")

#T3
tracks = {p["track"] for p in par}
print("\nTracks to offer in this year: ")
print(", ".join(tracks))
if len(tracks) < 2:
    print("No more tracks to offer.")

#T4
names = set()
dup = set()
for p in par:
    if p["name"] in names:
        dup.add(p["name"])
    names.add(p["name"])

if dup:
    for i in dup:
        print(f"Duplicated name: {i}")
else:
    print("No duplicated names.")