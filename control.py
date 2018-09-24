animals = ['dog','cat','lion','tiger']
for animal in animals:
    print(animal,len(animal))
    print(animal[0].upper() + animal[1:].lower())
    print(animal.capitalize())