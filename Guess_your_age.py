print("Hello, I'm Bob")
Name = input("Your name ?")
print("Hello", Name)
Current_Year = 2025
Birth_Year = int(input("What's your birth year ?"))
Age = Current_Year - Birth_Year
if Age < 18 :
    print(Name, "You are a minor" + "," +str(Age))
else:
    print(Name, "You are an adult" + ", " + str(Age))