message = input (">")
words = message.split(' ')

emojis = {
    ":)" : "😊",
    ":(" : "☹"

}
converter = ""
for ch in words:
    converter += emojis.get(ch, ch) + " "

print(converter)
