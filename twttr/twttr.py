text = input("Input: ")
for letter in text:
    if letter.lower() in ["a","e","i","o","u"]:
        text = text.replace(letter,"")
print(text)