name = input("Enter your name")

city = input("Enter your city name:")
# print("I am from ",city)

# I want to do whenever I want to format the string in a certain way 
# input(f"I am from {city}")
# "f" means formatted. 
# input(f"Hello friends, This is {name} and I am from {city}")


about = f"Hello friends, This is {name} and I am from {city}"

other_name = input("Enter the other person name:")
# print(about)
print(about.replace("friends", other_name))

print(dir(about))