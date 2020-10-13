'''
# Without parameters
def greet_user():
    print("Welcome on board")
    print("This is just the beginning")


print("Start")
greet_user()
print("Finish")


# With parameters
def greet_user2(name):
    print("Hi %s" % (name))
    print("Welcome onboard")


print("Start")
greet_user2("Temitope")
print("Finish")

'''

# With 2 parameters
def greet_user3(first_name, last_name):
    print("Hi %s %s" % (first_name, last_name))
    print("Welcome onboard")


print("Start")
greet_user3("Temi", "Tope")
print("Finish")



