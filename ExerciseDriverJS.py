from ProgramExerciseJS import Fancyshopping


food = Fancyshopping("Dry Cured Iberian Ham", 2)

print(food.calculate1())


def howmanyitems():
    mylist = []
    askuser = int(input("How many items will you order today?"))
    if askuser > 0:
        for i in range(askuser):
            print(f"Item #{i}")
            enterfood = input("Enter food: ")
            enteramtpound = int(input("Enter amount of pounds: "))
            mylist.append(Fancyshopping(enterfood,enteramtpound))

    else:
        print("error number must be positive")
    return mylist

mylist = howmanyitems()


def calculate(mylist):
    for item in mylist:
        print(f"Food: {item.foodname}, Amount: {item.calculate1()}")



calculate(mylist)

