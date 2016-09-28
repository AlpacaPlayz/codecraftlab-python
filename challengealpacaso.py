
directory = {"Nico": 94.2, "Jason": 98.7, "Leo": 54.6}
def search(name):
    print(directory[name])
def add(name, grade):
    directory[name] = grade
    print(directory)
def delete(name):
    del directory[name]
    print(directory)
answer = input("What do you want to do?")
if answer == "search":
    answer = input("What demigod's file do you want to see?")
    search(answer)
elif answer  == "add":
    answer1 = input("What demigod's file do you want to add?")
    answer2 = input("What is the demigod's grade?")
    add(answer1, answer2)

elif answer == "delete":
    answer3 = input("What demigod's file do you want to delete?")
    delete(answer3)
else:
    print("!FUNCTION NOT FOUND!")
