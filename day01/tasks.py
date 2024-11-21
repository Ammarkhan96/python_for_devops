import os
# print(dir(os))
print(os.uname().sysname)

def check_os(opsystem):
    if opsystem == "Windows":
        print("Switch to Linux")
    elif opsystem == "Linux" or opsystem =="Mac":
        print("you are good to go")


#I want run this function again and again
# for i in range(1, 5):
# for i in range(0, 5):
#     check_os("Linux")