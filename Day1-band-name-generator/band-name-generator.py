# Greet the user
print("Don't know what to name your band? Precisely do that here! Welcome!")
# Ask user for city name
city = input("What is your city name?\n")
univ = input("What is your university name?\n")
pet = input("What is your pet's name?\n")
# Band names
bandname1 = city +'\'s '+ pet
bandname2 = univ +'\'s '+ pet
bandname3 = city + ' ' + pet
print(f'Your Band name could be \n1. {bandname1} \n2. {bandname2} \n3. {bandname3}')