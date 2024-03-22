years = (1987, 1985, 1981, 1996)
a=len(years)
print(a)
b=sum(years)
print(b)
c=sorted(years)
print(c)

# tuples does not changes its elements onece it was write it was not changed by using append in list it was changed by using append

german_cars = ["porsche", "audi", "bmw"]
european_cars = ("ferrari", "volvo", "renault", german_cars)
print(european_cars)
european_cars[3].append("mercedes") #change list na under thay aetle error nai aaptu
print(german_cars)
print(european_cars)

fish_weight_kg = (("white_shark", 520), ("beluga", 1571), ("greenland_shark", 1400))
fish_weight_kg_dict = dict(fish_weight_kg)
print(fish_weight_kg_dict)


founding_year = {"Google":1996, "Apple":1976, "Sony":1946, "ebay":1995, "IBM":1911}
for company, year in founding_year.items():
    print(f"{company} was found in the year {year}")

channels = ("ngc", "discovery", "animal_planet", "history", "ngc")
a=channels.count("ngc")
print(a)
b=channels.index("history")
print(b)

t=12345,54321,'hello'
print(t)
x,y,z=t
print(x,y,z)
