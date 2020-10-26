try:
    name = input("Name : ")
    age = int(input("Age : "))
    income = int(input("Income : "))
    bonus = income / age
    print("My name is %s and I am %s. I am entitle to %s bonus" %(name, age, bonus))
except(ZeroDivisionError):
    print("Age cannot be Zero")
except(ValueError):
    print("Invalid Value")