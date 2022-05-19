import datetime
import math

Name = "Kacper"
Surname = "Bukowski"

Age = 22
Year = 1999

print(Name)
print(Surname)

#Napisz program wypisujący ze zmiennej "Name" twoje imię oraz ze zmiennej "Surname" twoje nazwisko

# (z nauczycielem) Napisz program wypisujący na konsolę aktualną datę i godzinę wykorzystując bibliotekę datetime

#Konkatenacja
# Twoje imie: <imie> Twoje nazwisko: <nazwisko>
# Dzisiaj jest: <data>
# Masz <Wiek> lata i urodziłeś się w roku <Rok>
print(Name + Surname)
print("Twoje imie: " + Name + "\nTwoje nazwisko: " + Surname)
print("Dzisiaj jest: " + str(datetime.datetime.now()))
#Sposób 1
print("Masz " + str(Age) + " lata i urodziłeś się w roku " + str(Year))
#Sposób 2
print(f"Masz {Age} lata i urodziłeś się w roku {Year}")

# Operatory matematyczne
print(Age+Year)
print(Year-Age)
print(Age-Year)
print(Year*Age)
print(Year/Age)
print(Age**2)
print(81//2)
print(81%2)
print(math.sqrt(81))
