print("Welcome to SMIT TechFest!")
print("Event organized by Jhon Rouge Andales of APPDAET BTCS2")

n_par = int(input("How many participants will register?: "))

if n_par <= 0:
    print("Invalid number of participants.")
    quit()

par = []
for i in range(n_par):
    name = input("Enter participant name: ")
    track = input("Enter a track: ")
    par.append({"name": name,"track": track})

print("registered participants: ")
for i, p in enumerate(par,1):
    print(f"{i}. {p['name']} - {p['track']}")