def emoji_converter(message):
    
    words = message.split(' ')

    emojis = {
        ":)" : "😊",
        ":(" : "☹"

    }
    converter = ""
    for ch in words:
        converter += emojis.get(ch, ch) + " "
    return converter


message = input (">")
convert = emoji_converter(message)
print(convert)
#print(emoji_converter(message))
