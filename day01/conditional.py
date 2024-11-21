# a = 100
# b = 30
# c = 50

# if a > b: #if this line is true then only the control flow goes down.
    # print("A is bigger")
    # print("Yes, I want to tell again A is bigger")
# else: #if the above "if condition" fails, then it goes to else
    # print("B is bigger")
# this four spaces is known as "Indentation".



env = "dev"
if env == "dev":
    print("Load dev application")
else:
    print("Not in dev environment")



a = 100
b = 30
c = 50

if a > b: #if this line is true then only the control flow goes down.
     print("A is bigger")
     print("Yes, I want to tell again A is bigger")
elif b > a and b > c:
    print("B is bigger")
elif c > a and c > b:
    print("c is the biggest")
else :
    print("all are equal")
