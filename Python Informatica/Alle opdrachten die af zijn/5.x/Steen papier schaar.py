from random import randint

print("Steen, papier, schaar!")
a = int(input("1 = Steen, 2 = Papier, 3 = Schaar"))

b = randint(1,3)

if a == b:
    print ("Gelijk!")
    
if a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1:
    print ("Loser!!! Ben je echt zo slecht!")
    
if a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2:
    print ("Dit was een inkompotje dat telt niet!")