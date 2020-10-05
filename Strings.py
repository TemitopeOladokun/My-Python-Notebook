message = 'Hello Temi, How are you ?'
print(message)


message2 = "Hello Helena, check this article for Jess's line of thought"
print(message2)


message3 = '''

Hello Uncle,

    How are you doing ? I am really excited about our upcoming project.
Hurray!!!

Yours Sincerely,
Temitope.

'''
print(message3)


print(message[0:10:2])


first = "John"
last = "Smith"

sentence = first + ' [' + last + '] is a coder'   #not so ideal for complicated task
print(sentence)

sentence2 = '%s %s is a coder' %(first, last)
print(sentence2)


# String Methods

Birthday = "Happy Birthday to you Mum"
# Upper case methods
print(Birthday.upper())

#Find methods
print(Birthday.find('a'))
print(Birthday.find('Birthday'))

Birthday2 = "Happy Birthday to you Mum"
print(Birthday2.capitalize())

print( len(Birthday2))

#Replace method
print(Birthday2.replace('Birthday', 'Felicitation'))

Birthday3 = "Happy Birthday to you Mum"
#Lower case method
print(Birthday3.lower())

# Title method
print(Birthday3.title())

# in operator
print("Mum" in Birthday3)






